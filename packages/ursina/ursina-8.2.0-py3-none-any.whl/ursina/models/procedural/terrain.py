from ursina import *


def texture_to_height_values(heightmap:Texture, skip=1):
    from numpy import asarray, flip, swapaxes
    from PIL import Image

    heightmap = heightmap
    skip = skip    # should be power of two. only works with heightmap, not height_values.

    if not isinstance(heightmap, Texture):
        heightmap = load_texture(heightmap)
        if not heightmap:
            print('failed to load heightmap:', heightmap)
            return

    width, depth = heightmap.width//skip, heightmap.height//skip
    img = heightmap.to_PIL_Image().convert('L')
    if skip > 1:
        img = img.resize([width, depth], Image.LANCZOS)

    height_values = asarray(img)
    height_values = flip(height_values, axis=0)
    height_values = swapaxes(height_values, 0, 1)
    return height_values



class Terrain(Mesh):
    def __init__(self, heightmap='', height_values=None, gradient=None, skip=1, **kwargs):

        if heightmap:
            self.height_values = texture_to_height_values(heightmap, skip)

        elif height_values is not None:
            self.height_values = height_values


        self.width = len(self.height_values)
        self.depth = len(self.height_values[0])
        self.aspect_ratio = self.width / self.depth
        self.gradient = gradient
        super().__init__()
        self.generate()


    def generate(self):
        # copy this from Plane to avoid unnecessary init
        self.vertices = []
        self.triangles = []
        self.uvs = []
        self.normals = []

        _height_values = [[j/255 for j in i] for i in self.height_values]
        w, h = self.width, self.depth
        centering_offset = Vec2(-.5, -.5)
        dx = 1/(w-1)
        dz = 1/(h-1)

        # create the plane
        i = 0
        for z in range(h):
            for x in range(w):

                self.vertices.append(Vec3((x/(w-1))+(centering_offset.x), _height_values[x][z], (z/(h-1))+centering_offset.y))
                self.uvs.append((x/w, z/h))

                if x > 0 and z > 0:
                    self.triangles.append((i, i-1, i-w-1, i-w-0))

                # normals
                if x > 0 and z > 0 and x < w-1 and z < h-1:
                    rl =  (_height_values[x+1][z] - _height_values[x-1][z]) / (2*dx)
                    fb =  (_height_values[x][z+1] - _height_values[x][z-1]) / (2*dz)
                    self.normals.append(Vec3(-rl, 1, -fb).normalized())
                else:
                    self.normals.append(Vec3(0,1,0))

                i += 1

        if self.gradient:
            self.colors = []
            for z, column in enumerate(self.height_values):
                for x, row in enumerate(column):
                    self.vertices.append(Vec3(x/w, self.height_values[x][z], z/h) + Vec3(centering_offset.x, 0, centering_offset.y))
                    y = int(self.height_values[x][z]*1)
                    y = clamp(y, 0, 255)
                    self.colors.append(self.gradient[y])


        super().generate()



if __name__ == '__main__':
    from ursina.shaders.normals_shader import normals_shader
    app = Ursina()
    '''Terrain using an RGB texture as input'''
    terrain_from_heightmap_texture = Entity(model=Terrain('heightmap_1', skip=8), scale=(40,5,20), texture='heightmap_1')

    '''
    I'm just getting the height values from the previous terrain as an example, but you can provide your own.
    It should be a list of lists, where each value is between 0 and 255.
    '''
    hv = terrain_from_heightmap_texture.model.height_values.tolist()
    terrain_from_list = Entity(model=Terrain(height_values=hv), scale=(40,40,40), texture='heightmap_1', x=40, shader=normals_shader)
    terrain_bounds = Entity(model='wireframe_cube', origin_y=-.5, scale=(40,40,40), color=color.lime)
    Entity(model='cube', shader=normals_shader, y=8, scale=4)
    def input(key):
        if key == 'space':  # randomize the terrain
            terrain_from_list.model.height_values = [[random.uniform(0,255) for a in column] for column in terrain_from_list.model.height_values]
            terrain_from_list.model.generate()

    EditorCamera(rotation_x=90)
    camera.orthographic = True
    Sky()
    player = Entity(model='sphere', color=color.azure, scale=.2, origin_y=-.5)

    def update():
        direction = Vec3(held_keys['d'] - held_keys['a'], 0, held_keys['w'] - held_keys['s']).normalized()
        player.position += direction * time.dt * 8
        y = terraincast(player.world_position, terrain_from_list, terrain_from_list.model.height_values)
        if y is not None:
            player.y = y





    app.run()
