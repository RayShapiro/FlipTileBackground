tiles.setTilemap(tilemap`level`)
game.onUpdateInterval(500, function on_update_interval() {
    myTiles.tile1.flipY()
    myTiles.tile2.flipX()
})
