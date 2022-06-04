

def is_collided(
        alien_x_coordinates, alien_y_coordinates,
        bullet_x_coordinates, bullet_y_coordinates):
    distance = (
        (alien_x_coordinates - bullet_x_coordinates)**2 +
        (alien_y_coordinates - bullet_y_coordinates)**2
    ) ** 0.5
    if distance < 27:
        return True
    return False
