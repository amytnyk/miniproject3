[![Pylint](https://github.com/amytnyk/miniproject3/actions/workflows/pylint.yml/badge.svg)](https://github.com/amytnyk/miniproject3/actions/workflows/pylint.yml)
## Algorithm
### Introducton
The basic idea is to surround the opponent, so he won't be able to make a move. It can be done by using heatmaps where every tile is the length of the shortest path to the nearest opponent's tile.
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
* At the beginning stack contains coordinates of the opponent's tiles
* At each iteration, we set the level value to tiles that are adjacent to any of the tiles in the stack
* The stack in the next iteration will contain all modified tiles from the previous iteration
### Placing figure
* Let's the score of the figure be the sum of all values on the heatmap which are covered by new figure
```python
score = 0
for row_idx, col_idx in iterate_filled_fields(figure):
    score += heatmap[move[0] + row_idx][move[1] + col_idx]
return score
```
* The figure that is nearest to the opponent will have the lowest score, so from all possible figures we need to choose the lowest
```python
heatmap = create_heatmap(board)
scores = map(lambda move: (get_score(heatmap, figure, move), move), positions)

return min(scores)[1]
```
## Visualization
![Image](./assets/res.gif)
* This is the game between my bot and another.
* To run visualizer use command:
```
python visualizer/visualizer.py -file path/to/game/dump.txt -image /path/to/animation.gif
```
## Credits
* The concept and colors of the visualization were actually grabbed from https://github.com/Lcharvol/Filler