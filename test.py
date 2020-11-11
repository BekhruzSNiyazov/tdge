import tdge

game = tdge.Game(movement=True, width=10, height=10, title="Hello, test", resizable=True)

tdge.display.set_background(game, background_type="image", image_path="C:/Users/Niyazov/Desktop/SUKHAYL/IMAGES/STOCK/earth.jpg")
tdge.display.draw_cube(game, size=(1, 1, 1), coords=(1, 1, 1), color=(0, 0, 255))
tdge.start_game(game)
