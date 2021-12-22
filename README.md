## Algorithm
### Introducton
The basic idea is to surround the opponent so he won't be able to make a move. It's can be done by using heatmaps where every tile is the length of the shortest path to nearest opponents tile.
### Implementation
```python
level = 1
while stack:
        new_stack = []
        for py, px in stack:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = px + dx, py + dy
                if 0 <= x < width and 0 <= y < height and heatmap[y][x] > level:
                    new_stack.append((y, x))
                    heatmap[y][x] = level
        level += 1
        stack, new_stack = new_stack, []
```
* At the beginning stack contains coordinates of the opponents tiles
* At each iteration we set the level value to tiles which are adjacent to any of tiles in stack
### Placing figure
* Let's the score of the figure be the sum of all values on the heatmap which are covered by new figure
```python
score = 0
for row_idx, col_idx in iterate_filled_fields(figure):
    score += heatmap[move[0] + row_idx][move[1] + col_idx]
return score
```
* The figure that is nearest to opponent will have the lowest score, so from all possible figures we need to choose lowest
## Visualization
![Image](./assets/res.gif)
* This is the game between my bot and another.
* To run visualizer use command:
```
python visualizer/visualizer.py -file path/to/game/dump.txt -image /path/to/animation.gif
```
## Credits
* The concept and colors of the visualization were actually grabbed from https://github.com/Lcharvol/Filler