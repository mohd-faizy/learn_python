# Publishing a Python Package to PyPI using UV: Part-1

This guide documents the end-to-end journey of creating, troubleshooting, and successfully publishing a Python package (`autoedapkd`) to PyPI using `uv`. 

---

### Step 1: Initialize the Project
**The Action:** We started by initializing a new Python package.
```bash
uv init --package autoeda
cd autoeda
```

**Project State:**
* **Before:** Empty directory.
* **After:** `uv` scaffolded a standard project structure:
  ```
  autoeda/
  ├── src/
  │   └── autoeda/
  │       └── __init__.py
  ├── .gitignore
  ├── .python-version
  ├── pyproject.toml
  └── README.md
  ```

---

### Step 2: Add Dependencies
**The Action:** We added the necessary libraries for data analysis and visualization.
```bash
uv add pandas numpy matplotlib seaborn
```

**Project State:**
* **Before:** `pyproject.toml` had an empty `dependencies = []` block.
* **After:** A `uv.lock` file was generated, and the dependencies were added to `pyproject.toml`:
  ```toml
  dependencies = [
      "matplotlib>=3.11.0",
      "numpy>=2.5.1",
      "pandas>=3.0.3",
      "seaborn>=0.13.2",
  ]
  ```

---

### Step 3: Build the Package
**The Action:** Once the code was ready, we generated the distribution archives.
```bash
uv build
```

**Project State:**
* **Before:** No distribution files existed.
* **After:** A new `dist/` folder was created containing the `.tar.gz` and `.whl` files:
  ```
  dist/
  ├── autoeda-0.1.0-py3-none-any.whl
  └── autoeda-0.1.0.tar.gz
  ```

---

### Step 4: Generating a PyPI API Token
Before publishing, an API token is required.
1. Log in to [pypi.org](https://pypi.org)
2. Go to **Account settings** → **API tokens**
3. Click **Add API token**, choose the scope, and generate it.
> [!IMPORTANT]
> PyPI shows the token only once — copy and store it securely.

---

### Step 5: Initial Publish Attempt (Error)
**The Action:** We attempted to upload the package to PyPI.
```bash
uv publish --token <YOUR_TOKEN>
```

**Project State:**
* **Result:** The upload **failed** with a `403 Forbidden` error:
  `403 The user 'faizymohd' isn't allowed to upload to project 'autoeda'.`
* **Why:** The name `autoeda` was already taken by someone else on PyPI.

---

### Step 6: Fix the Name Conflict
**The Action:** We had to rename the package to something unique (`autoedapkd`). We updated the `name` field in `pyproject.toml`, and then renamed the module directory to match.
```bash
# Rename the source directory to match the new package name
mv src/autoeda src/autoedapkd
```

**Project State:**
* **Before:** Module was located at `src/autoeda/` and `pyproject.toml` used `name = "autoeda"`.
* **After:** Module moved to `src/autoedapkd/` and `pyproject.toml` updated:
  ```toml
  name = "autoedapkd"
  ...
  [project.scripts]
  autoeda = "autoedapkd:main"
  ```

---

### Step 7: Clean and Rebuild
**The Action:** We removed the old `dist` files and built the new renamed package.
```bash
rm -rf dist
uv build
```

**Project State:**
* **Before:** `dist/` contained the old `autoeda` files.
* **After:** `dist/` was refreshed with the new `autoedapkd` distribution files:
  ```
  dist/
  ├── autoedapkd-0.1.0-py3-none-any.whl
  └── autoedapkd-0.1.0.tar.gz
  ```

---

### Step 8: Successful Publication
**The Action:** We ran the publish command one final time.
```bash
uv publish --token <YOUR_TOKEN>
```

**Project State:**
* **Before:** Wheels sat unpublished in the `dist` folder.
* **After:** The package `autoedapkd` was successfully uploaded to PyPI and became available for anyone to install via `pip install autoedapkd`!

<br>
<br>

---

# Publishing an Updated Version: Part 2


When you make changes to your code and want to release a new version of your package, follow these steps:

### Step 1: Bump the Version Number
**The Action:** You must increase the version number in `pyproject.toml`. PyPI does not allow you to overwrite an existing version.
* Open `pyproject.toml`
* Change `version = "0.1.0"` to `version = "0.1.1"` (or your next version).

**Project State:**
* **Before:** `version = "0.1.0"`
* **After:** `version = "0.1.1"`

---

### Step 2: Clean the Old Builds
**The Action:** Remove the old distribution files so you don't accidentally try to upload them again.
```bash
rm -rf dist
```

**Project State:**
* **Before:** `dist/` contains version 0.1.0 files.
* **After:** `dist/` directory is completely removed.

---

### Step 3: Build the New Version
**The Action:** Generate the new distribution archives for the updated version.
```bash
uv build
```

**Project State:**
* **Before:** No `dist/` directory exists.
* **After:** A new `dist/` folder is created with the updated version files:
  ```
  dist/
  ├── autoedapkd-0.1.1-py3-none-any.whl
  └── autoedapkd-0.1.1.tar.gz
  ```

---

### Step 4: Publish the Update
**The Action:** Upload the new version to PyPI using your token.
```bash
uv publish --token <YOUR_TOKEN>
```

**Project State:**
* **Before:** New wheels sit unpublished.
* **After:** Version `0.1.1` is successfully uploaded to PyPI. Users can now run `pip install --upgrade autoedapkd` to get the latest features!


