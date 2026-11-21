# Contributing Guidelines

Thank you for contributing to this project! To keep our repository clean, readable, and easy to navigate, please follow the commit message conventions and tooling setup outlined below.

---

## Commit Message Convention

All commit messages **must be written in English** and strictly follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Format

```text
<type>(<scope>): <short description>

[optional body]
```

### Rules

1. **Language:** Always write commit messages in English.
2. **Type:** Must be one of the following:
   - `feat`: A new feature
   - `fix`: A bug fix
   - `docs`: Documentation only changes
   - `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc.)
   - `refactor`: A code change that neither fixes a bug nor adds a feature
   - `perf`: A code change that improves performance
   - `test`: Adding missing tests or correcting existing tests
   - `build`: Changes that affect the build system or external dependencies
   - `ci`: Changes to our CI configuration files and scripts
   - `chore`: Other changes that do not modify `src` or `test` files
3. **Scope (optional):** A noun describing a section of the codebase surrounded by parentheses (e.g., `feat(auth):`, `fix(api):`).
4. **Description:**
   - Use the **imperative, present tense** (e.g., `"add"` instead of `"added"` or `"adds"`).
   - Do not capitalize the first letter.
   - Do not end the subject line with a period (`.`).
   - Keep the entire subject line under **50 characters**.
5. **Body (optional):** If the commit introduces complex changes or modifies multiple files, add a blank line after the subject and include a concise bullet-point list explaining *what* changed and *why*, wrapped at **72 characters**.

### Examples

```text
feat(auth): add password reset endpoint
```

```text
fix(cart): prevent negative item quantities

- Add validation check before updating cart state
- Display warning toast when quantity reaches zero
```

---

## Automated Commit Messages with GitHub Copilot

This repository is pre-configured so that GitHub Copilot automatically follows our commit message rules when generating commit messages in VS Code.

### How It Works

1. **Instruction File (`.github/commit-instructions.md`):** Contains the exact prompt rules enforcing English and Conventional Commits.
2. **Workspace Settings (`.vscode/settings.json`):** Instructs VS Code's Source Control commit generator to read `.github/commit-instructions.md`.

### Usage in VS Code

1. Stage your changes in the **Source Control** panel (`Ctrl+Shift+G` / `Cmd+Shift+G`).
2. Click the **Generate Commit Message** (sparkle ✨) icon inside the commit message input box.
3. Review the generated message to ensure accuracy before committing.

*(Note: If you use Copilot Chat or Copilot Agents, general repository guidelines in `AGENTS.md` or `.github/copilot-instructions.md` will also enforce English across code, comments, and documentation.)*