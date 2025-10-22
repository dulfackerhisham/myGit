
# myGit
building my own git

## 🧠 Understanding This Line of Code in init()

```python
write_file(os.path.join(myGitRepo, '.git', 'HEAD'), b'ref: refs/heads/master')
````

This line creates a file called `.git/HEAD` and writes this inside it:

```
ref: refs/heads/master
```

That means → **“The current branch is `master`, and its reference is stored in `.git/refs/heads/master`.”**

---

### 🧩 Explanation (Simplified)

| Part                        | Meaning                                                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `b'ref: refs/heads/master'` | The `b` means **bytes literal** → data is written as **raw bytes** instead of text. (Binary mode = writing exact 0s and 1s, not characters.) |
| `'wb'`                      | **Write Binary Mode** → allows writing bytes to the file. (Text mode `'w'` is for normal strings.)                                           |
| `ref:`                      | Git-specific keyword → tells Git this file **points to another reference file**.                                                             |
| `.git/HEAD`                 | Shows which **branch** you’re currently on.                                                                                                  |
| `.git/refs/heads/master`    | Stores the **commit hash** of the `master` branch.                                                                                           |

---

### 🧾 In Simple Words

When you run your `init("hdRepo")`:

* It makes folders just like Git does.
* Then writes `ref: refs/heads/master` in `.git/HEAD`, meaning:

  > “You’re now on the master branch.”
---

---

## 🧱 Git Index (Staging Area)

The **Git Index**, also called the **staging area**, is a file (`.git/index`) that tracks the files you want to include in your next commit.

It’s like a **temporary list** that tells Git:
> “These are the files I’m preparing to commit.”

---

### 🧩 How It Works

- The index is stored in a **custom binary format** (not plain text).
- It contains information like:
  - File name (path)
  - File size
  - Modification time
  - SHA-1 hash (unique fingerprint of file)
- The index always lists **all files in the current tree**, not just the newly added ones.

---
---

### 🧩 Explanation (Simplified)

| Concept         | Meaning                                                                 |
| ---------------- | ----------------------------------------------------------------------- |
| `.git/index`     | A **binary file** that stores info about files staged for commit        |
| `struct.unpack()` | Reads **binary data** into readable Python values                      |
| `b'DIRC'`        | The **signature** that identifies this file as a Git index              |
| `num_entries`    | The total number of files being tracked                                 |
| `try / except`   | Prevents crashes if `.git/index` file doesn’t exist                     |
| `assert`         | Double-checks that the file structure is **valid**                      |

---