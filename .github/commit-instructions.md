Generate commit messages strictly in English, following the Conventional Commits specification:
- Format: `<type>(<scope>): <short description>`
- Allowed types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`.
- Use the imperative, present tense in the description (e.g., "add" not "added" or "adds").
- Do not capitalize the first letter of the description and do not end it with a period.
- Keep the subject line under 50 characters.
- If the changes are complex or touch multiple files, include a concise bullet-point body explaining *what* changed and *why*, wrapped at 72 characters.