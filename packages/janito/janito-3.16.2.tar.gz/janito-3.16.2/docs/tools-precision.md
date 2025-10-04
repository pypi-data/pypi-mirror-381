# Precision in Context Construction: Outlines, Search, and Token Optimization

Large Language Models (LLMs) like those used in Janito are powerful, but their effectiveness depends heavily on the quality and relevance of the context provided to them. Precision in context construction is crucial for:

- Improving the model’s attention and accuracy.
- Reducing irrelevant information (noise).
- Optimizing the use of available tokens (which are limited per request).

## Why Precision Matters

LLMs have a fixed token limit for each prompt. Supplying too much irrelevant or excessive context can:

- Waste valuable tokens.
- Dilute the model’s focus, leading to less accurate or less relevant responses.

By contrast, providing only the most relevant code, documentation, or data enables the LLM to:

- Focus its attention on what matters for the current task.
- Produce more accurate, actionable, and context-aware outputs.

## How Janito Achieves Precision

Janito uses a combination of **outline** and **search** utilities to extract only the most relevant portions of code or documentation:

### 1. Outline Utilities

- **Purpose:** Quickly analyze the structure of files (e.g., Python modules, Markdown docs) to identify classes, functions, methods, headers, and sections.
- **How it works:**
  - The outline tool parses the file and builds a map of its structure.
  - This enables Janito to select specific ranges (e.g., a single function, class, or section) rather than the entire file.
- **Benefits:**
  - Enables targeted extraction.
  - Reduces the amount of irrelevant context.

### 2. Search Utilities

- **Purpose:** Find precise locations of keywords, function names, class names, or documentation headers within files or across the project.
- **How it works:**
  - The search tool can use substring or regex matching to locate relevant lines or blocks.
  - Results are mapped to file ranges or outline nodes, allowing for precise extraction.
- **Benefits:**
  - Supports both broad and fine-grained queries.
  - Can be combined with outline data for even more accurate targeting.

## Building Tailored Contexts

When Janito receives a request (e.g., "Refactor function X" or "Summarize section Y"), it:

1. **Uses outline and search tools** to locate the exact code or documentation range relevant to the task.
2. **Extracts only that range** (plus minimal necessary context, such as imports or docstrings).
3. **Constructs the LLM prompt** using just the tailored content, not the entire file or project.

## Benefits for LLM Attention and Token Efficiency

- **Improved Attention:** The LLM can focus on the most relevant code or documentation, leading to better understanding and more accurate results.
- **Token Optimization:** By sending only what’s needed, Janito avoids hitting token limits and can handle larger projects or more complex tasks within the same constraints.
- **Faster, More Relevant Responses:** Less noise means the model can reason more effectively and respond more quickly.

## Summary

Janito’s precision-driven approach—using outline and search utilities to extract and assemble only the most relevant context—maximizes the effectiveness of LLMs. This ensures:

- Higher quality answers.
- Better use of computational resources.
- A more scalable and robust developer experience.

