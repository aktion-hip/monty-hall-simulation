# Ziegenproblem Simulation

(vgl. https://www.andinet.de/raetsel/mathematik/dreitore.html) (engl. [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem))

Lösungsansatz mit *Domain Driven Design (DDD)*:

Objekte:
```
Stage
Stage.setStrategy(Strategy)
Stage.runFirst(randomDoorNr)
Stage.runFinal() => 1/0
```

```
Door
Door.setWinner(boolean)
```

```
Strategy
Strategy.process(door_selected_in_first_run, other_door) -> door_selected_final
```

Simulation:
```
def run_simulation(strategy, max = 100):
    print(f"Running simulation with strategy: {strategy}, (number of runs: {max})")
    score = 0
    for _ in range(1, max):
        stage = Stage()
        stage.setStrategy(strategy)
        stage.runFirst(random.randint(0, 2))
        score += stage.runFinal()
    print(f"Score: {score} / {max} (with Strategy: {strategy})")
```
