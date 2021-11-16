## Basic Ideas

- 2D simulation software that simulates the lifespan of animals and plants
- 2D terrain generation
- Prey vs. Predators
- Different foods give different benefits (the rarer they are, the more nutritious they are)
- Animals can starve
- Clicking on an animal will kill and it make it dissapear 
- Will be able to change attributes that will have a direct impact on the simulation
  - Avg. lifespan of animal1, animal2, animal3, etc.
  - Avg. plant/food growth
  - Avg. offspring rates of each animal
  - Avg. rainfall/water levels
  - Initial animal population
  - Avg. mutability rate of each animal
  - Change the speed of the simulation or go through it step-by-step
  - Graph the current population of each animal type, current amount of food present, current terrain type present
  
## Far-fetched ideas

  - Weather can impact the terrain, and therefore impact the animals and food levels
  - Everything can impact and/or interact with everything 
    - Wolves eat sheep (this is basic functionality)
    - Wolves and foxes can eat each other, or they can gang up with each other 
    - No bees? Then there's no plants!
    - As animals drink water, the terrain is updated to reflect that 
  - Stray humans may wander into the land. Safe to say that they probably won't make it back home...
    - A gang of humans could then come into the land and try to fight the animals 
    - Add tombstone 
  - Make 2D terrain have height (like hills), instead of birds-eye view. Think like Terraria.
    - Animate the animals jumping from one level to another 
  - Really far-fetched idea: 3D terrain 
  - Climate Change kills everything

## Animals

- Wolves
  -  Offspring rate 
  -  Hunger rate
  -  Thirst rate
  -  Average lifespan (don't let them live past 80 cycles or something)
  -  Mutation rate/chance
  -  Mutation status
  -  Nutritional Value
  -  Speed
- Sheep
  -  Offspring rate
  -  Hunger rate
  -  Thirst rate
  -  Average lifespan (don't let them live past 80 cycles or something)
  -  Mutation rate/chance
  -  Mutation status
  -  Nutritional Value
  -  Speed
- Bunnies
- Bees
- Foxes
- Bears
- Frogs
- Birds

## Terrain types

- Forest
- Mountains
- Flat-land

## Mutations

- Double the size (require more food, more water, harder to kill, stronger, slower, etc.)
- Half the size (require less food, less, water, easier to kill, weaker, faster, etc.)
- CANNIBALISM
- If water is present, they just swim happily until they pass away
- Can only eat certain food
- Different colors
  - Red, Blue, Orange sheep
- Diseased
  - Maybe signify by making them green?
  - Can spread the disease
  - If sick enough, can be ostracized from pack
  - Fun idea: put a mask on them if they are sick
- Can get pregnant on their own 
- Can give birth to other kinds of animals 
- Doesn't need food and/or water
- Dies 3 cycles after being born 
 
## Implementation

- OOP for all animals and plants, possibly even terrain
  - All animals will have:
    -  Offspring rate (baby/cycles)
    -  Hunger level
    -  Thirst level
    -  Health level
    -  Hunger rate (decrese in 
    -  Thirst rate
    -  Average lifespan (don't let them live past 80 cycles or something)
    -  Current age
    -  Mutation rate/chance
    -  Mutation status
    -  Nutritional Value
    -  Speed
- Terrain
  - Start with 2D grid (2D list)
  - Randomize color of cells 
    - Green: Grass
    - Brown: No grass
    - Blue: Water
    - White: Snow
    - Bright colors: flowers
    
