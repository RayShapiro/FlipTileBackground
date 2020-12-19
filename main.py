

my_flipped = False

tiles.set_tilemap(tilemap("""level"""))

def on_update_interval():
    console.log_value("z", my_flipped)
    myTiles.tile1.flipX()
    myTiles.tile2.flipX()
game.on_update_interval(500, on_update_interval)

mytiles = [sprites.builtin.shark0, 
            sprites.builtin.shark1, 
            sprites.builtin.shark2,
            sprites.builtin.shark3]

my_sprite = sprites.create(sprites.builtin.shark0, SpriteKind.player)
scene.camera_follow_sprite(my_sprite)
controller.move_sprite(my_sprite,0)
my_sprite.set_velocity(-15, 0)

animation.run_image_animation(my_sprite, mytiles, 300, True)

def on_button_r():
    global my_flipped

    if (my_flipped == True):
        return 
    else:
        my_flipped = True

    my_sprite.set_velocity(15, 0)
    for s in mytiles:
        s.flip_x()

controller.player1.on_button_event(ControllerButton.LEFT, ControllerButtonEvent.PRESSED, on_button_l)

def on_button_l():
    global my_flipped

    if (my_flipped == False):
        return
    else:
        my_flipped = False

    my_sprite.set_velocity(-15, 0)
    for s in mytiles:
        s.flip_x()

controller.player1.on_button_event(ControllerButton.RIGHT, ControllerButtonEvent.PRESSED, on_button_r)