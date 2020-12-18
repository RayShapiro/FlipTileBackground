tiles.set_tilemap(tilemap("""level"""))

def on_update_interval():
    myTiles.tile1.flipY()
    myTiles.tile2.flipX()
game.on_update_interval(500, on_update_interval)
