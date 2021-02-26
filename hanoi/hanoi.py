
def hanoi(disk: int, src: str, dest: str, center: str):
    if disk < 1:
        return

    hanoi(disk-1, src, center, dest)
    print(f'{disk} move {src} to {dest}')
    hanoi(disk-1, center, dest, src)


hanoi(3, 'A', 'C', 'B')
