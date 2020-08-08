# Interview Prep for Multi Interaction


### For a fully functional environment on repl.it visit: [Interview Prep](https://repl.it/@CarterJin/Interview-Prep)

### How to run

Before you start, create a <your name>.txt file under Descriptions and put in your question description in there in comments

```bash
  ./pair.sh (insert as many participant names)
```
Head to `questions/` to see .java files created for each person. Edit in the file of your name. When you want to test run, do `./sol.sh (your name)` to run the file that is corresponding to your name

### After your session

```bash
  ./done.sh (date)
```
to save all questions content to a file under PastQuestions and will remove today's content


### User Settings

You can now have a <your name>.setting.json file under the UserSettings directory with a field: `"preferredLanguage": "<java or python>" `
which would get picked up when making matches

if you set python as your preferredLanguage, when calling sol.sh you have to do: `./sol.sh -p <your name> `