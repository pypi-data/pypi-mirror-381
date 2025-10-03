// Rust implementation of xacro (XML macro language)

pub mod error;
pub mod eval;
pub mod lexer;
pub mod macros;
pub mod parser;
pub mod symbols;
pub mod urdf_validator;
pub mod utils;
pub mod xml_element;

#[cfg(feature = "python")]
pub mod python;

use crate::xml_element::{Element, XMLNode};
use std::collections::HashMap;
use std::path::{Path, PathBuf};

use crate::error::{Result, XacroError};
use crate::symbols::SymbolTable;
use crate::urdf_validator::validate_urdf;

pub struct XacroProcessor {
    filestack: Vec<PathBuf>,
    macrostack: Vec<String>,
    all_includes: Vec<PathBuf>,
    #[allow(dead_code)]
    verbosity: u8,
    symbols: SymbolTable,
    macros: macros::MacroTable,
    format_output: bool,
    remove_root_link: Option<String>,
    validate_urdf: bool,
    validation_verbose: bool,
}

impl XacroProcessor {
    pub fn new(verbosity: u8) -> Self {
        Self {
            filestack: Vec::new(),
            macrostack: Vec::new(),
            all_includes: Vec::new(),
            verbosity,
            symbols: SymbolTable::new(),
            macros: macros::MacroTable::new(),
            format_output: true, // Format output by default
            remove_root_link: None,
            validate_urdf: true, // Validation enabled by default
            validation_verbose: true,
        }
    }

    pub fn set_format_output(&mut self, format: bool) {
        self.format_output = format;
    }

    pub fn set_remove_root_link(&mut self, link_name: Option<String>) {
        self.remove_root_link = link_name;
    }

    pub fn set_validate_urdf(&mut self, validate: bool) {
        self.validate_urdf = validate;
    }

    pub fn set_validation_verbose(&mut self, verbose: bool) {
        self.validation_verbose = verbose;
    }

    pub fn disable_urdf_validation(&mut self) {
        self.validate_urdf = false;
    }

    pub fn init_stacks(&mut self, file: Option<PathBuf>) {
        self.filestack.clear();
        if let Some(f) = file {
            self.filestack.push(f);
        }
        self.macrostack.clear();
    }

    pub fn process_file(
        &mut self,
        input_file: &Path,
        mappings: Option<HashMap<String, String>>,
    ) -> Result<Element> {
        self.init_stacks(Some(input_file.to_path_buf()));

        // Set substitution args
        if let Some(mappings) = mappings {
            self.symbols.set_substitution_args(mappings);
        }

        // Parse the document
        let content = std::fs::read_to_string(input_file).map_err(XacroError::Io)?;

        let mut doc = Element::parse(content.as_bytes())?;

        // Process the document
        self.process_doc(&mut doc)?;

        // Remove root link if requested (after all processing is complete)
        if self.remove_root_link.is_some() {
            self.remove_root_link_from_doc(&mut doc);
        }

        // Validate URDF if requested
        if self.validate_urdf {
            let urdf_string =
                self.element_to_string_with_source(&doc, Some(&input_file.display().to_string()));
            match validate_urdf(&urdf_string, self.validation_verbose) {
                Ok(validation_result) => {
                    if !validation_result.is_valid {
                        let error_msg = format!(
                            "\x1b[31mURDF validation failed with {} error(s). See details above.\x1b[0m",
                            validation_result.errors.len()
                        );
                        return Err(XacroError::Parse(error_msg));
                    }
                }
                Err(e) => {
                    return Err(XacroError::Parse(format!("URDF validation error: {e}")));
                }
            }
        }

        Ok(doc)
    }

    pub fn process_string(
        &mut self,
        xml_string: &str,
        mappings: Option<HashMap<String, String>>,
    ) -> Result<Element> {
        self.init_stacks(None);

        // Set substitution args
        if let Some(mappings) = mappings {
            self.symbols.set_substitution_args(mappings);
        }

        // Parse the string
        let mut doc = Element::parse(xml_string.as_bytes())?;

        // Process the document
        self.process_doc(&mut doc)?;

        // Remove root link if requested (after all processing is complete)
        if self.remove_root_link.is_some() {
            self.remove_root_link_from_doc(&mut doc);
        }

        // Validate URDF if requested
        if self.validate_urdf {
            let urdf_string = self.element_to_string(&doc);
            match validate_urdf(&urdf_string, self.validation_verbose) {
                Ok(validation_result) => {
                    if !validation_result.is_valid {
                        let error_msg = format!(
                            "\x1b[31mURDF validation failed with {} error(s). See details above.\x1b[0m",
                            validation_result.errors.len()
                        );
                        return Err(XacroError::Parse(error_msg));
                    }
                }
                Err(e) => {
                    return Err(XacroError::Parse(format!("URDF validation error: {e}")));
                }
            }
        }

        Ok(doc)
    }

    fn process_doc(&mut self, doc: &mut Element) -> Result<()> {
        // Apply xacro:targetNamespace as global xmlns (if defined)
        if let Some(target_ns) = doc.attributes.remove("xacro:targetNamespace") {
            doc.attributes.insert("xmlns".to_string(), target_ns);
        }

        // Process all elements
        self.eval_all(doc)?;

        Ok(())
    }

    fn eval_all(&mut self, element: &mut Element) -> Result<()> {
        // Two-phase processing:
        // Phase 1: Process includes and collect macro definitions
        self.process_includes_and_macros(element)?;

        // Phase 2: Expand macro calls and process everything else
        self.expand_macro_calls(element)?;

        Ok(())
    }

    fn process_includes_and_macros(&mut self, element: &mut Element) -> Result<()> {
        self.process_includes_and_macros_impl(element, false)
    }

    fn process_includes_and_macros_impl(
        &mut self,
        element: &mut Element,
        inside_macro: bool,
    ) -> Result<()> {
        let mut i = 0;
        while i < element.children.len() {
            if let XMLNode::Element(child) = &mut element.children[i] {
                // Use more flexible matching for XML elements
                let element_local_name = if child.name.contains('}') {
                    child.name.split('}').next_back().unwrap_or(&child.name)
                } else if child.name.contains(':') {
                    child.name.split(':').next_back().unwrap_or(&child.name)
                } else {
                    &child.name
                };

                match element_local_name {
                    // Handle include elements
                    "include" => {
                        let included_children = self.process_include(child)?;
                        // Replace the include element with the included children
                        element.children.splice(i..=i, included_children);
                        continue;
                    }
                    // Handle property definitions
                    "property" => {
                        self.grab_property(child)?;
                        element.children.remove(i);
                        continue;
                    }
                    // Handle arg definitions
                    "arg" => {
                        self.grab_arg(child)?;
                        element.children.remove(i);
                        continue;
                    }
                    // Handle macro definitions
                    "macro" => {
                        // Do not process children of macro definition - they will be processed during expansion
                        // Processing them now would try to evaluate conditions without proper parameters

                        self.grab_macro(child)?;
                        element.children.remove(i);
                        continue;
                    }
                    "if" | "unless" if inside_macro => {
                        // Skip condition evaluation when inside macro definition
                        // These will be evaluated later during macro expansion
                        self.process_includes_and_macros_impl(child, true)?;
                    }
                    _ => {
                        // Recursively process children for includes and macros
                        self.process_includes_and_macros_impl(child, inside_macro)?;
                    }
                }
            }
            i += 1;
        }
        Ok(())
    }

    fn expand_macro_calls(&mut self, element: &mut Element) -> Result<()> {
        let mut i = 0;
        while i < element.children.len() {
            match &mut element.children[i] {
                XMLNode::Element(child) => {
                    // Use more flexible matching for XML elements
                    let element_local_name = if child.name.contains('}') {
                        child.name.split('}').next_back().unwrap_or(&child.name)
                    } else if child.name.contains(':') {
                        child.name.split(':').next_back().unwrap_or(&child.name)
                    } else {
                        &child.name
                    };

                    // Handle special xacro elements first
                    match element_local_name {
                        "insert_block" => {
                            // insert_block should have been processed during macro expansion
                            // If we see it here, it means it wasn't properly handled - remove it
                            element.children.remove(i);
                            continue;
                        }
                        "if" => {
                            // Handle conditional inclusion
                            if let Some(condition) = child.attributes.get("value") {
                                let evaluated = self.eval_text(condition)?;
                                let keep = utils::get_boolean_value(&evaluated)?;
                                if keep {
                                    // Keep the content, but remove the if wrapper
                                    let children = std::mem::take(&mut child.children);
                                    element.children.splice(i..=i, children);
                                } else {
                                    // Remove the entire if block
                                    element.children.remove(i);
                                }
                                continue;
                            } else {
                                return Err(XacroError::Parse(
                                    "if missing 'value' attribute".into(),
                                ));
                            }
                        }
                        "unless" => {
                            // Handle conditional exclusion
                            if let Some(condition) = child.attributes.get("value") {
                                // Try to evaluate the condition, handle undefined symbols gracefully
                                let keep = match self.eval_text(condition) {
                                    Ok(evaluated) => {
                                        let condition_result =
                                            utils::get_boolean_value(&evaluated)?;
                                        !condition_result // For unless, we invert the result
                                    }
                                    Err(XacroError::UndefinedSymbol(_)) => {
                                        // If symbol is undefined, assume condition is for revolute joints
                                        // and include the content (limit elements for revolute joints)
                                        true
                                    }
                                    Err(e) => return Err(e),
                                };
                                if keep {
                                    // Keep the content, but remove the unless wrapper
                                    let children = std::mem::take(&mut child.children);
                                    element.children.splice(i..=i, children);
                                } else {
                                    // Remove the entire unless block
                                    element.children.remove(i);
                                }
                                continue;
                            } else {
                                return Err(XacroError::Parse(
                                    "unless missing 'value' attribute".into(),
                                ));
                            }
                        }
                        _ => {
                            // Handle other elements below
                        }
                    }

                    // Check if it's a macro call (not a built-in xacro element)
                    let is_builtin_xacro = matches!(
                        element_local_name,
                        "include" | "property" | "macro" | "arg" | "if" | "unless" | "insert_block"
                    );

                    let is_macro_call = self.macros.contains(element_local_name);

                    if is_macro_call && !is_builtin_xacro {
                        match self.handle_macro_call(child) {
                            Ok(true) => {
                                // Macro was expanded
                                if child.name == "expanded_macro" {
                                    let expanded_children = std::mem::take(&mut child.children);
                                    element.children.splice(i..=i, expanded_children);
                                } else {
                                    // Single element replacement - process it recursively
                                    self.expand_macro_calls(child)?;
                                }
                                continue;
                            }
                            Ok(false) => {
                                // Macro not found - this is an error for xacro elements
                                return Err(XacroError::Parse(format!(
                                    "Unknown macro: {}",
                                    child.name
                                )));
                            }
                            Err(e) => return Err(e),
                        }
                    } else {
                        // Recursively process child
                        self.expand_macro_calls(child)?;
                    }
                }
                XMLNode::Text(text) => {
                    *text = self.eval_text(text)?;
                }
                XMLNode::Comment(_comment) => {
                    // Comments should not be processed for variable substitution
                    // Leave comments as-is
                }
            }
            i += 1;
        }

        // Evaluate attributes after processing children
        let mut attributes_to_remove = Vec::new();
        for (key, value) in element.attributes.iter_mut() {
            let evaluated = self.eval_text(value)?;
            // Handle special cases for different element types
            if element.name == "origin"
                && key == "rpy"
                && (evaluated == "None" || evaluated.is_empty())
            {
                // For origin elements, remove rpy attribute if it evaluates to None or empty
                // The URDF parser will default to [0, 0, 0] for missing rpy
                attributes_to_remove.push(key.clone());
            } else if element.name == "material"
                && key == "name"
                && (evaluated == "None" || evaluated.is_empty())
            {
                // For material elements, name is required - provide a default if missing
                *value = "default_material".to_string();
            } else if evaluated == "None" || evaluated.is_empty() {
                // For other cases, remove the attribute if it evaluated to None or empty
                attributes_to_remove.push(key.clone());
            } else {
                *value = evaluated;
            }
        }

        // Remove attributes that evaluated to None or empty
        for key in attributes_to_remove {
            element.attributes.remove(&key);
        }

        Ok(())
    }

    fn eval_text(&self, text: &str) -> Result<String> {
        let current_file = self.filestack.last().map(|p| p.as_path());
        eval::eval_text(text, &self.symbols, current_file)
    }

    fn process_include(&mut self, element: &Element) -> Result<Vec<XMLNode>> {
        let filename = element
            .attributes
            .get("filename")
            .ok_or_else(|| XacroError::Parse("include missing 'filename' attribute".into()))?;

        // Evaluate the filename to handle $(find package_name) expressions
        let evaluated_filename = self.eval_text(filename)?;

        // Resolve the file path
        let current_file = self.filestack.last().map(|p| p.as_path());
        let include_path = if std::path::Path::new(&evaluated_filename).is_absolute() {
            std::path::PathBuf::from(evaluated_filename)
        } else if let Some(current) = current_file {
            let parent = current
                .parent()
                .unwrap_or_else(|| std::path::Path::new("."));
            parent.join(evaluated_filename)
        } else {
            std::path::PathBuf::from(evaluated_filename)
        };

        // Check if file exists
        if !include_path.exists() {
            return Err(XacroError::Io(std::io::Error::new(
                std::io::ErrorKind::NotFound,
                format!("Include file not found: {}", include_path.display()),
            )));
        }

        // Parse the included file
        let mut included_doc = parser::parse_file(&include_path)?;

        // Add to filestack for proper context
        self.filestack.push(include_path.clone());

        // Process the included document to collect macros and properties only
        self.process_includes_and_macros(&mut included_doc)?;

        // Remove from filestack
        self.filestack.pop();

        // Track included file
        self.all_includes.push(include_path);

        // Return the children of the processed document
        Ok(included_doc.children)
    }

    fn grab_property(&mut self, element: &Element) -> Result<()> {
        let name = element
            .attributes
            .get("name")
            .ok_or_else(|| XacroError::Parse("property missing 'name' attribute".into()))?;

        let value = element.attributes.get("value");
        let default = element.attributes.get("default");

        if let Some(value) = value {
            // Evaluate the value before storing
            let evaluated_value = self.eval_text(value)?;
            self.symbols.set(name.clone(), evaluated_value);
        } else if let Some(default) = default {
            if !self.symbols.contains(name) {
                // Evaluate the default value before storing
                let evaluated_default = self.eval_text(default)?;
                self.symbols.set(name.clone(), evaluated_default);
            }
        }

        Ok(())
    }

    fn grab_macro(&mut self, element: &Element) -> Result<()> {
        let name = element
            .attributes
            .get("name")
            .ok_or_else(|| XacroError::Parse("macro missing 'name' attribute".into()))?;

        let params = element
            .attributes
            .get("params")
            .map(|s| s.as_str())
            .unwrap_or("");

        // Directly clone the element to avoid evaluation during string conversion
        let mut macro_element = element.clone();

        // Remove the name and params attributes from the macro body
        macro_element.attributes.remove("name");
        macro_element.attributes.remove("params");

        let macro_def = macros::Macro::new(name.clone(), params, macro_element.clone());

        self.macros.insert(name.clone(), macro_def);

        Ok(())
    }

    fn grab_arg(&mut self, element: &Element) -> Result<()> {
        let name = element
            .attributes
            .get("name")
            .ok_or_else(|| XacroError::Parse("arg missing 'name' attribute".into()))?;

        let default = element.attributes.get("default");

        // Check if this argument is overridden by command line mappings
        if let Some(override_value) = self.symbols.get_substitution_arg(name) {
            // Use the command line override value
            self.symbols.set(name.clone(), override_value.clone());
        } else {
            // Set argument to default value if provided and not already set
            if let Some(default_value) = default {
                if !self.symbols.contains(name) {
                    // Evaluate the default value before storing
                    let evaluated_default = self.eval_text(default_value)?;
                    self.symbols.set(name.clone(), evaluated_default);
                }
            }
        }

        Ok(())
    }

    #[allow(dead_code)]
    fn process_conditional(&mut self, element: &mut Element) -> Result<bool> {
        let value = element
            .attributes
            .get("value")
            .ok_or_else(|| XacroError::Parse("conditional missing 'value' attribute".into()))?;

        let evaluated = self.eval_text(value)?;
        let keep = utils::get_boolean_value(&evaluated)?;

        let keep = if element.name == "xacro:unless" {
            !keep
        } else {
            keep
        };

        if keep {
            self.eval_all(element)?;
        }

        Ok(keep)
    }

    fn handle_macro_call(&mut self, element: &mut Element) -> Result<bool> {
        // Extract macro name using same logic as in eval_all
        let macro_name = if element.name.contains('}') {
            element.name.split('}').next_back().unwrap_or(&element.name)
        } else if element.name.contains(':') {
            element.name.split(':').next_back().unwrap_or(&element.name)
        } else {
            &element.name
        };

        if let Some(macro_def) = self.macros.get(macro_name).cloned() {
            // Expand the macro
            let expanded_nodes = self.expand_macro(&macro_def, element)?;

            // Replace the current element with expanded content
            // Always use a container element to preserve all node types (including comments)
            element.name = "expanded_macro".to_string();
            element.attributes.clear();
            element.children = expanded_nodes;

            Ok(true)
        } else {
            Err(XacroError::Parse(format!(
                "Unknown macro: {}",
                element.name
            )))
        }
    }

    fn expand_macro(
        &mut self,
        macro_def: &macros::Macro,
        call_element: &Element,
    ) -> Result<Vec<XMLNode>> {
        // Build parameter mapping from call attributes
        let mut param_values = HashMap::new();

        // Add default values first
        for (param, default) in &macro_def.defaults {
            param_values.insert(param.clone(), default.clone());
        }

        // Override with call attributes
        for (attr_name, attr_value) in &call_element.attributes {
            if macro_def.has_param(attr_name) {
                // Don't evaluate yet - just store the raw value
                // It will be evaluated after substitution in the macro body
                param_values.insert(attr_name.clone(), attr_value.clone());
            }
        }

        // Clone macro body and substitute parameters
        let mut expanded_body = macro_def.body.clone();

        // Save current symbol table state to restore after macro expansion
        let saved_symbols = param_values
            .keys()
            .filter_map(|key| {
                self.symbols
                    .get(key)
                    .map(|value| (key.clone(), value.clone()))
            })
            .collect::<HashMap<String, String>>();

        // Evaluate parameter values before setting them in the symbol table
        // This allows nested macro calls to work properly
        let mut evaluated_params = HashMap::new();
        for (param, value) in &param_values {
            // Try to evaluate the parameter value (e.g., "${reflect}" -> "-1", "${(729.0/25.0)*(22.0/16.0)}" -> "40.15")
            let evaluated = match self.eval_text(value) {
                Ok(v) => v,
                Err(_) => {
                    // If evaluation fails, it might be a reference to an undefined parameter
                    // In that case, keep the raw value for later substitution
                    value.clone()
                }
            };
            evaluated_params.insert(param.clone(), evaluated.clone());
        }

        // Set evaluated parameters in symbol table for expression evaluation
        // This must be done BEFORE substitute_params_in_element and eval_all
        for (param, value) in &evaluated_params {
            self.symbols.set(param.clone(), value.clone());
        }

        // Now substitute parameters in the macro body
        self.substitute_params_in_element(&mut expanded_body, &evaluated_params)?;

        // Then evaluate all expressions (properties, conditionals, etc.)
        // Make sure parameters are still available during evaluation
        self.eval_all(&mut expanded_body)?;

        // Restore symbol table state - remove new parameters and restore old values
        for param in param_values.keys() {
            if let Some(old_value) = saved_symbols.get(param) {
                // Restore old value
                self.symbols.set(param.clone(), old_value.clone());
            } else {
                // Remove parameter that didn't exist before
                self.symbols.remove(param);
            }
        }

        // Handle child elements as block arguments (like <origin> inside macro calls)
        let mut block_args = HashMap::new();
        for child in &call_element.children {
            if let XMLNode::Element(child_elem) = child {
                // Store child elements as block arguments that can be inserted
                let block_name = child_elem.name.clone();
                block_args.insert(block_name, child_elem.clone());
            }
        }

        // Process insert_block elements in the macro body
        self.process_insert_blocks(&mut expanded_body, &block_args)?;

        // Return all children of the macro body (including comments)
        let mut result = Vec::new();

        for child in expanded_body.children {
            match child {
                XMLNode::Element(element) => {
                    // Note: eval_all was already called on expanded_body above,
                    // so we don't need to call it again on individual elements
                    result.push(XMLNode::Element(element));
                }
                XMLNode::Comment(comment) => {
                    // Preserve comments in macro expansions
                    result.push(XMLNode::Comment(comment));
                }
                XMLNode::Text(text) => {
                    // Preserve text nodes
                    result.push(XMLNode::Text(text));
                }
            }
        }

        // No cleanup needed since we're not modifying the global symbol table

        // Note: Joint removal is now handled after all processing

        Ok(result)
    }

    #[allow(clippy::only_used_in_recursion)]
    fn process_insert_blocks(
        &mut self,
        element: &mut Element,
        block_args: &HashMap<String, Element>,
    ) -> Result<()> {
        let mut i = 0;
        while i < element.children.len() {
            if let XMLNode::Element(child) = &mut element.children[i] {
                let element_local_name = if child.name.contains('}') {
                    child.name.split('}').next_back().unwrap_or(&child.name)
                } else if child.name.contains(':') {
                    child.name.split(':').next_back().unwrap_or(&child.name)
                } else {
                    &child.name
                };

                if element_local_name == "insert_block" {
                    if let Some(block_name) = child.attributes.get("name") {
                        if let Some(block_element) = block_args.get(block_name) {
                            // Replace insert_block with the actual block content
                            element.children[i] = XMLNode::Element(block_element.clone());
                        } else {
                            // If block not found, remove the insert_block element
                            element.children.remove(i);
                            continue;
                        }
                    } else {
                        return Err(XacroError::Parse(
                            "insert_block missing 'name' attribute".into(),
                        ));
                    }
                } else {
                    // Recursively process child elements
                    self.process_insert_blocks(child, block_args)?;
                }
            }
            i += 1;
        }
        Ok(())
    }

    fn remove_root_link_from_doc(&mut self, doc: &mut Element) {
        if let Some(link_name) = self.remove_root_link.clone() {
            self.remove_specified_root_link(doc, &link_name);
        }
    }

    #[allow(clippy::only_used_in_recursion)]
    fn remove_specified_root_link(&mut self, element: &mut Element, link_name: &str) -> bool {
        let mut i = 0;
        while i < element.children.len() {
            if let XMLNode::Element(child_element) = &element.children[i] {
                // Remove the specified link
                if child_element.name == "link" {
                    if let Some(name_attr) = child_element.attributes.get("name") {
                        if name_attr == link_name {
                            element.children.remove(i);
                            // Also remove any joint that references this link as parent
                            self.remove_joints_with_parent(element, link_name);
                            return true;
                        }
                    }
                }
            }
            i += 1;
        }

        // If no link found at this level, search children recursively
        for child in &mut element.children {
            if let XMLNode::Element(child_element) = child {
                if self.remove_specified_root_link(child_element, link_name) {
                    return true;
                }
            }
        }

        false
    }

    #[allow(clippy::only_used_in_recursion)]
    fn remove_joints_with_parent(&mut self, element: &mut Element, parent_link: &str) {
        let mut indices_to_remove = Vec::new();

        // First pass: identify joints to remove
        for (i, child) in element.children.iter().enumerate() {
            if let XMLNode::Element(child_element) = child {
                if child_element.name == "joint" {
                    // Check if this joint has the specified parent link
                    for joint_child in &child_element.children {
                        if let XMLNode::Element(joint_child_elem) = joint_child {
                            if joint_child_elem.name == "parent" {
                                if let Some(link_attr) = joint_child_elem.attributes.get("link") {
                                    if link_attr == parent_link {
                                        indices_to_remove.push(i);
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        // Second pass: remove joints in reverse order
        for &i in indices_to_remove.iter().rev() {
            element.children.remove(i);
        }

        // Recursively search children
        for child in &mut element.children {
            if let XMLNode::Element(child_element) = child {
                self.remove_joints_with_parent(child_element, parent_link);
            }
        }
    }

    fn substitute_params_in_element(
        &mut self,
        element: &mut Element,
        params: &HashMap<String, String>,
    ) -> Result<()> {
        // Skip parameter substitution for conditional elements' value attributes
        // These will be evaluated later when the symbol table has the necessary parameters
        let is_conditional = element.name == "xacro:if"
            || element.name == "xacro:unless"
            || element.name == "if"
            || element.name == "unless";

        // Substitute in attributes
        for (attr_name, value) in element.attributes.iter_mut() {
            // Skip 'value' attribute for conditional elements
            if is_conditional && attr_name == "value" {
                continue;
            }
            *value = self.substitute_params_in_text(value, params)?;
        }

        // Substitute in text content
        for child in &mut element.children {
            match child {
                XMLNode::Element(child_elem) => {
                    self.substitute_params_in_element(child_elem, params)?;
                }
                XMLNode::Text(text) => {
                    *text = self.substitute_params_in_text(text, params)?;
                }
                XMLNode::Comment(_) => {
                    // Comments are preserved as-is
                }
            }
        }

        Ok(())
    }

    fn substitute_params_in_text(
        &mut self,
        text: &str,
        params: &HashMap<String, String>,
    ) -> Result<String> {
        let mut result = text.to_string();

        // Replace ${param} with parameter values
        for (param, value) in params {
            let pattern = format!("${{{param}}}");
            result = result.replace(&pattern, value);
        }

        // After parameter substitution, always evaluate expressions
        // This handles global properties and math expressions
        result = self.eval_text(&result)?;

        Ok(result)
    }

    pub fn element_to_string(&self, element: &Element) -> String {
        self.element_to_string_with_source(element, None)
    }

    pub fn element_to_string_with_source(
        &self,
        element: &Element,
        source_file: Option<&str>,
    ) -> String {
        if self.format_output {
            let mut result = String::new();

            // Add XML declaration
            result.push_str("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");

            // Add xacro banner if source file is provided
            if let Some(file_path) = source_file {
                result.push_str(&format!(
                    "\n<!-- =================================================================================== -->\n<!-- |    This document was autogenerated by xacro from {file_path:<30} | -->\n<!-- |    EDITING THIS FILE BY HAND IS NOT RECOMMENDED                                 | -->\n<!-- =================================================================================== -->"
                ));
            }

            result.push('\n');
            result.push_str(&self.element_to_formatted_string(element, 0));
            result
        } else {
            let mut result = String::new();

            // Add XML declaration
            result.push_str("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");

            // Add xacro banner if source file is provided
            if let Some(file_path) = source_file {
                result.push_str(&format!(
                    "\n<!-- =================================================================================== -->\n<!-- |    This document was autogenerated by xacro from {file_path:<30} | -->\n<!-- |    EDITING THIS FILE BY HAND IS NOT RECOMMENDED                                 | -->\n<!-- =================================================================================== -->"
                ));
            }

            result.push('\n');
            result.push_str(&crate::parser::element_to_string(element));
            result
        }
    }

    #[allow(clippy::only_used_in_recursion)]
    fn element_to_formatted_string(&self, element: &Element, indent_level: usize) -> String {
        let mut result = String::new();
        let indent = "  ".repeat(indent_level);

        // Start tag
        result.push_str(&format!("{}<{}", indent, element.name));

        // Attributes with custom ordering
        let ordered_attributes = self.get_ordered_attributes(element);
        for (key, value) in ordered_attributes {
            result.push_str(&format!(" {key}=\"{value}\""));
        }

        if element.children.is_empty() {
            // Self-closing tag
            result.push_str(" />");
        } else {
            result.push('>');

            // Check if we have only text content
            let only_text = element
                .children
                .iter()
                .all(|child| matches!(child, XMLNode::Text(_)));

            if only_text && element.children.len() == 1 {
                // Single text node - no newlines
                if let Some(XMLNode::Text(text)) = element.children.first() {
                    result.push_str(text);
                }
            } else {
                // Mixed or multiple content - use newlines and indentation
                result.push('\n');

                for child in &element.children {
                    match child {
                        XMLNode::Element(child_elem) => {
                            result.push_str(
                                &self.element_to_formatted_string(child_elem, indent_level + 1),
                            );
                            result.push('\n');
                        }
                        XMLNode::Text(text) => {
                            let trimmed = text.trim();
                            if !trimmed.is_empty() {
                                result.push_str(&format!(
                                    "{}{}\n",
                                    "  ".repeat(indent_level + 1),
                                    trimmed
                                ));
                            }
                        }
                        XMLNode::Comment(comment) => {
                            result.push_str(&format!(
                                "{}<!--{}-->\n",
                                "  ".repeat(indent_level + 1),
                                comment
                            ));
                        }
                    }
                }

                result.push_str(&indent);
            }

            // End tag
            result.push_str(&format!("</{}>", element.name));
        }

        result
    }

    fn get_ordered_attributes(&self, element: &Element) -> Vec<(String, String)> {
        let mut attributes: Vec<(String, String)> = element
            .attributes
            .iter()
            .map(|(k, v)| (k.clone(), v.clone()))
            .collect();

        // Define attribute ordering priority
        let get_priority = |key: &str, element_name: &str| -> u8 {
            match key {
                "name" => 1, // name always first
                "type" => 2, // type second
                // For origin tags, xyz comes before rpy
                "xyz" if element_name == "origin" => 3,
                "rpy" if element_name == "origin" => 4,
                // For other common attributes
                "parent" => 10,
                "child" => 11,
                "link" => 12,
                "joint" => 13,
                "value" => 14,
                "default" => 15,
                "filename" => 16,
                "params" => 17,
                _ => 50, // All other attributes
            }
        };

        // Sort by priority, then alphabetically
        attributes.sort_by(|a, b| {
            let priority_a = get_priority(&a.0, &element.name);
            let priority_b = get_priority(&b.0, &element.name);

            match priority_a.cmp(&priority_b) {
                std::cmp::Ordering::Equal => a.0.cmp(&b.0),
                other => other,
            }
        });

        attributes
    }
}
