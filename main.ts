let my_flipped = false
tiles.setTilemap(tilemap`level`)
game.onUpdateInterval(500, function on_update_interval() {
    console.logValue("z", my_flipped)
    myTiles.tile1.flipX()
    myTiles.tile2.flipX()
})
let mytiles = [sprites.builtin.shark0, sprites.builtin.shark1, sprites.builtin.shark2, sprites.builtin.shark3]
let my_sprite = sprites.create(sprites.builtin.shark0, SpriteKind.Player)
scene.cameraFollowSprite(my_sprite)
controller.moveSprite(my_sprite, 0)
my_sprite.setVelocity(-15, 0)
animation.runImageAnimation(my_sprite, mytiles, 300, true)
controller.player1.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function on_button_l() {
    
    if (my_flipped == false) {
        return
    } else {
        my_flipped = false
    }
    
    my_sprite.setVelocity(-15, 0)
    for (let s of mytiles) {
        s.flipX()
    }
})
controller.player1.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function on_button_r() {
    
    if (my_flipped == true) {
        return
    } else {
        my_flipped = true
    }
    
    my_sprite.setVelocity(15, 0)
    for (let s of mytiles) {
        s.flipX()
    }
})
