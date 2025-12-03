# Pull Shark Badge Guide 🦈

## What you need: Merge 2 pull requests

### Method 1: Using GitHub Web Interface (Easiest)

**First Pull Request:**
1. Go to your GitHub repository
2. Click on a file (like README.md)
3. Click the pencil icon to edit
4. Make any small change (add a line, fix typo, etc.)
5. Scroll down and select "Create a new branch for this commit and start a pull request"
6. Name it something like `update-1`
7. Click "Propose changes"
8. Click "Create pull request"
9. Click "Merge pull request"
10. Click "Confirm merge"

**Second Pull Request:**
11. Repeat steps 2-10 with a different change
12. Name the branch `update-2`

✅ **Done!** The Pull Shark badge should appear on your profile soon.

---

### Method 2: Using Git Commands (If you prefer terminal)

```bash
# First PR
git checkout -b feature-1
echo "Change 1" >> test.txt
git add test.txt
git commit -m "Add feature 1"
git push origin feature-1
# Go to GitHub, create PR, and merge it

# Second PR
git checkout main
git pull
git checkout -b feature-2
echo "Change 2" >> test.txt
git add test.txt
git commit -m "Add feature 2"
git push origin feature-2
# Go to GitHub, create PR, and merge it
```

---

## Tips:
- Use any repository you own
- The changes can be tiny (even just adding a space)
- Both PRs must be merged (not just created)
- Takes about 2-3 minutes total
