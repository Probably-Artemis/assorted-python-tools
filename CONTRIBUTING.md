# Contributing
## Ground rules

Any and all contributions are welcome, as long as they follow a few small and simple rules. I welcome bug fixes, documentation improvements, and new features. <ins>This is a side project, so replies may take a week or two.</ins>

1. An issue must be present. If an issue is not present, you can open an issue.
2. **Follow the [AI Policy](#ai-policy).**
3. For new features, provide at least one example use case in your issue.
4. Read the sections below. This list is only a quick summary.

## Before you start

Please make sure to check existing issues and pull requests before creating either, to avoid duplication. Comment on an issue and claim it before starting to work on it. If a claim has gone two weeks with no updates, it is considered stale and no longer valid.

## Setup

Use Python 3.13+ and install with python -m pip install -e . in a venv, from the root of your cloned fork. As of writing, no test suite exists, so describe how you checked your work in the PR. For more in-depth instructions, see the [long installation instructions](https://github.com/Probably-Artemis/assorted-python-tools#long-instructions).

## Making changes

For the sake of neatness and convenience, please work on a branch of your fork, not your fork's `main`. Please limit yourself to one fix or feature per issue or PR.

Please document your code. Any public function needs a reST-style docstring. Every module needs a section in the README. If you worry you would not be able to write good documentation, for example if English is not your first language, contact me and I will document for you. Mentioning me in a comment is sufficient contact.

## Reporting bugs

In your issue, please list the steps to reproduce, expected result, actual result, Python version, and OS. Beyond that, you may supply any extra information you wish to.

## Pull request expectations

1. Make sure to link to the issue you fix. For example, if I were writing a PR that fixes issue number 42, I would put `Fixes #42` in the body of my PR.
2. Please note what you changed and how it was tested.

## AI Policy

You must declare any and all usage of AI clearly and unmistakably. I may ask you to explain what your code does if I believe you have used AI. If I suspect you used AI and did not disclose it, I will not accept your work. 

AI usage ranges from inline suggestions or asking a chatbot questions to having an agent process the entire PR from reading the issue all the way to opening the request. No matter how it was used, it must be declared.

Declare any use of AI at the very top of your issue or pull request's body. Use the format of this example:
```
AI USAGE DISCLAIMER: Blorbo AI was used to generate variable names.
```
I will not immediately dispose of work you have disclosed as AI, but I will be more cautious.

## Licensing

As this project is under the MIT License, by contributing you agree that your work is released under the MIT License.