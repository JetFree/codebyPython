import pyglet

vidPath = 'Need_for_Speed.mp4'
window = pyglet.window.Window(1280, 720)
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)

player.queue(MediaLoad)
player.play()


@window.event
def on_draw():
    window.clear()
    if player.source and player.source.video_format:
        player.get_texture().blit(0, 0)


def print_msg(is_success):
    lines_range = range(0, 18)
    if is_success:
        lines_range = range(19, 30)
    with open("result.txt", "r") as file:
        lines = file.readlines()
        for i in lines_range:
            print(lines[i], end="")


if __name__ == "__main__":
    pyglet.app.run()
    if (bet := int(input("Сделайте ставку, выберите маршрут 1 или 2: "))) == 2:
        print_msg(True)
    elif bet == 1:
        print_msg(False)
    else:
        print("Необходимо выбрать значение 1 или 2!")
