#### Tweaking Speed

Type the following command in Console and press enter. You can use any other speed in place of 1000.

```js
Runner.instance_.setSpeed(1000)
```



#### Immortality

After every command press enter. All the commands are case-sensitive.

We store the original game over function in a variable:

```js
var original = Runner.prototype.gameOver
```

Then, we make the game over function empty:

```js
Runner.prototype.gameOver = function(){}
```

Stopping the game after using Immortality

When you want to stop the game, Revert back to the original game over function:

```js
Runner.prototype.gameOver = original
```



#### Setting the current score

Let’s set the score to 12345. You can set any other score less than 99999. The current score is reset on game over.

```js
Runner.instance_.distanceRan = 12345 / Runner.instance_.distanceMeter.config.COEFFICIENT
```



#### Dino jumping too high?

You can control how high the dino jumps by using the below function. Adjust the value as necessary.

```js
Runner.instance_.tRex.setJumpVelocity(10)
```



[Source](https://gist.github.com/JARVIS-AI/cfb916c7dc3bea73abf0edac42749ea8)
