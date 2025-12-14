# The fortress a Secure Reverse Proxy
> The Objective: Building a secure "Castle"

1. The Gate (Nginx): A public-facing server that accepts traffic from the internet
2. The Treasury (Python Backend): A private server that holds the data/logic.

**The rule**: The "Treasury" must be **invisible** to the outside world. No one can access it directly via `localhost:5000`.
They must go through the Nginx "Gate" at `localhost:8080`.

[Link para los comandos basicos git](https://training.github.com/downloads/es_ES/github-git-cheat-sheet.pdf)  
[Link sintaxis de escritura y formatos basicos de markdown](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
