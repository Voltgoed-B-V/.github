# Development Tools

## IDE

Ik (Casper) gebruik en heb een voorkeur voor Visual Studio Code. Het is light-weight en kan naar voorkeur uitgebreid worden met extensies.

### VSCODE-extensies

* mypy, checkt Python typing
  * Vereist: installeer mypy package met `pip install mypy`
* Rainbow CSV
* markdownlint
* Markdown Preview Enhanced, kan markdown files previews omzetten naar o.a. `.html` en `.pdf`.
* Flake8, checkt Python formatting

## Lettertype

Persoonlijk groot fan van _IntelOne Mono_. `

## Environment Variables

Om in Windows environment variables makkelijk en veilig toe te voegen kan je dit doen via je `$profile`. Typ in Powershell `$profile` dan krijg je een bestandslocatie terug, deze bestaat waarschijnlijk nog niet en moet je zelf even maken. Als je daarna dit bestand opent kan je er environment variables aan toevoegen. Je moet de naam altijd prefixen met "\$env:" dus bijvoorbeeld `$env:GITHUB_TOKEN='...'`. Je kan ook folders aan PATH toevoegen met `$env:Path += ';C:\Users\CasperKole\Documents\Programs'`

## Git

We werken met Git repositories op GitHub. Deze werken met 1 branch _main_, waarbij gebruik wordt gemaakt van  [Semantic Release](https://github.com/semantic-release/semantic-release) om verschillende versies bij te houden.

Om iets nieuws te implementeren open je een nieuwe branch. als deze klaar is om in main te stoppen voer je eerst `git pull origin develop` om eventuele merge problemen met de _main_ branch op te lossen.  Hierna is het goed om je commits zoveel mogelijk squashen, dit is het makkelijkst via `git rebase -i HEAD~X`. waar X het aantal commits in je branch is. Vergeet niet hierna `git push -f` te doen om de rebase te pushen.  Hierna kan je een pull request doen en zouden er geen problemen zijn nadat deze goedgekeurd is.

### _Commit Messages_

Voor Semantic Release moeten we een specifiek _format_ voor commits gebruiken. Dit is de [Angular Commit Message Convention](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit-header). Hieronder volgt de deels aangepaste uitleg.

#### Commit Message Format

_This specification is inspired by and supersedes the AngularJS commit message format._

We have very precise rules over how our Git commit messages must be formatted.
This format leads to **easier to read commit history**.

Each commit message consists of a **header**, a **body**, and a **footer**.

```none
<header>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The `header` is mandatory.

The `body` is mandatory for all commits except for those of type "docs". When the body is present it must be at least 20 characters long.

The `footer` is optional.

##### Commit Message Header

```none
<type>(<scope>): <short summary>
  │       │             │
  │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─⫸ Commit Scope: What section of the code the change relates to.
  │
  └─⫸ Commit Type: build|ci|docs|feat|fix|perf|refactor|test
```

The `<type>` and `<summary>` fields are mandatory, the `(<scope>)` field is optional.

##### Type

Must be one of the following:

* **build**: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
* **ci**: Changes to our CI configuration files and scripts (examples: CircleCi, SauceLabs)
* **docs**: Documentation only changes
* **feat**: A new feature
* **fix**: A bug fix
* **perf**: A code change that improves performance
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **test**: Adding missing tests or correcting existing tests

##### Summary

Use the summary field to provide a succinct description of the change:

* use the imperative, present tense: "change" not "changed" nor "changes"
* don't capitalize the first letter
* no dot (.) at the end

#### Commit Message Body

Just as in the summary, use the imperative, present tense: "fix" not "fixed" nor "fixes".

Explain the motivation for the change in the commit message body. This commit message should explain _why_ you are making the change.
You can include a comparison of the previous behavior with the new behavior in order to illustrate the impact of the change.

#### Commit Message Footer

The footer can contain information about breaking changes and deprecations and is also the place to reference GitHub issues, Jira tickets, and other PRs that this commit closes or is related to.
For example:

```none
BREAKING CHANGE: <breaking change summary>
<BLANK LINE>
<breaking change description + migration instructions>
<BLANK LINE>
<BLANK LINE>
Fixes #<issue number>
```

or

```none
DEPRECATED: <what is deprecated>
<BLANK LINE>
<deprecation description + recommended update path>
<BLANK LINE>
<BLANK LINE>
Closes #<pr number>
```

Breaking Change section should start with the phrase "BREAKING CHANGE: " followed by a summary of the breaking change, a blank line, and a detailed description of the breaking change that also includes migration instructions.
