# vibe-cadding

This is a codex skill for vibe-cadding: a skill for codex to do programmatic agentic code-as-cad interactively with a UI inside the codex app.

It starts a webserver and prompts you to open Codex's built in browser and uses that to give you a 3D view and controls to adjust geometry. There is functionality to take a screen shot of the 3D view and annotate it ("add a hole here please") and send that to the agent. It also provides rendering tools to the agent to rerender at the same camera angle to confirm that it has done the work. 

As of May 2026, GPT 5.5 is... OK at cad. You often have to prompt it a few times and ask for things in pretty small steps, but you can build some complicated things.

# Installation: 

Who are we kidding: this is a vibe coding project. Just tell codex you want to install this skill and give it the link. #yolo. You will probably have to restart codex to for it to see the skill. 


# Manual usage: 

We both know you're not gonna do this. You're just gonna tell codex "I wanna vibe cad a new shelf-bracket-dragon-hat" and off you go. But just in case, here are some commands, or whatever.

Initialize a new example project with:

```bash
./scripts/init_example_project.sh my-project
```

That installs dependencies with `uv`, installs the Playwright browser runtime used by agent screenshots, and writes `projects/my-project/model.py`. The generated model starts from the bundled example model. Codex will replace it with whatever you want cadded up.

```bash
uv sync
uv run vibecad --model projects/my-project/model.py --host 127.0.0.1 --port 8000
```
