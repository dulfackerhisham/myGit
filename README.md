
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

