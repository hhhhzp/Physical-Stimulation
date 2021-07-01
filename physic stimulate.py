import itertools
import math
import os
import random
from math import acos, cos, pi, sin, sqrt

import pygame
import pymunk
import pymunk as pm
import pymunk.pygame_util
import pymunk.util as u
from pygame.color import *
from pygame.locals import *
from pymunk import Vec2d

__docformat__ = "reStructuredText"
white = 255, 255, 255


width, height = 600, 600
button_w = int(width/8)
button_h = int(height/24)
dis_left = int(width/12)
dis_right = int(width/24)
dis_v = int(height/20)
dis_h = int(height/12)
dis_v2 = int(height/30)
background = pygame.image.load("background.png")
background_size = pygame.transform.scale(background,(width, height))

model1 = pygame.image.load("model1.png")
model1_size = pygame.transform.scale(model1, (button_w, button_h))


model2 = pygame.image.load("model2.png")
model2_size = pygame.transform.scale(model2, (button_w, button_h))


model3 = pygame.image.load("model3.png")
model3_size = pygame.transform.scale(model3, (button_w, button_h))


model4 = pygame.image.load("model4.png")
model4_size = pygame.transform.scale(model4, (button_w, button_h))


model5 = pygame.image.load("model5.png")
model5_size = pygame.transform.scale(model5, (button_w, button_h))

model6 = pygame.image.load("model6.png")
model6_size = pygame.transform.scale(model6, (button_w, button_h))

back = pygame.image.load("back.png")
back_size = pygame.transform.scale(back, (button_w, button_h))

fourstars = pygame.image.load("circle_four.png")
fourstars_size = pygame.transform.scale(fourstars, (button_w, button_h))

threestars = pygame.image.load("line three.png")
threestars_size = pygame.transform.scale(threestars, (button_w, button_h))

threestars2 = pygame.image.load("circlethree.png")
threestars2_size = pygame.transform.scale(threestars2, (button_w, button_h))

fourstars2 = pygame.image.load("line  four.png")
fourstars2_size = pygame.transform.scale(fourstars2, (button_w, button_h))

icon = pygame.image.load("小球.png")
pygame.display.set_icon(icon)

class Button1(pygame.sprite.Sprite):
    def __init__(self):
        super(Button1, self).__init__()
        self.surf = pygame.Surface((button_w, button_h))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def check(self, mouse_pos):
        if mouse_pos[0] > dis_left and mouse_pos[0] < dis_left + button_w and mouse_pos[1] > dis_h and mouse_pos[1] < dis_h + button_h:
            return True
        else:
            return False

class Button2(pygame.sprite.Sprite):
    def __init__(self):
        super(Button2, self).__init__()
        self.surf = pygame.Surface((button_w, button_h))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def check(self, mouse_pos):
        if mouse_pos[0] > dis_left and mouse_pos[0] < dis_left + button_w and mouse_pos[1] > dis_h + button_h + dis_v and mouse_pos[1] < dis_h + 2*button_h + dis_v:
            return True
        else:
            return False

class Button3(pygame.sprite.Sprite):
    def __init__(self):
        super(Button3, self).__init__()
        self.surf = pygame.Surface((button_w, button_h))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def check(self, mouse_pos):
        if mouse_pos[0] > dis_left and mouse_pos[0] < dis_left + button_w and mouse_pos[1] > dis_h + 2*button_h + 2*dis_v and mouse_pos[1] < dis_h + 3*button_h + 2*dis_v:
            return True
        else:
            return False


class Button4(pygame.sprite.Sprite):
    def __init__(self):
        super(Button4, self).__init__()
        self.surf = pygame.Surface((button_w, button_h))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def check(self, mouse_pos):
        if mouse_pos[0] > dis_left and mouse_pos[0] < dis_left + button_w and mouse_pos[1] > dis_h + 3*button_h + 3*dis_v and mouse_pos[1] < dis_h + 4*button_h + 3*dis_v:
            return True
        else:
            return False


class Button5(pygame.sprite.Sprite):
    def __init__(self):
        super(Button5, self).__init__()
        self.surf = pygame.Surface((button_w, button_h))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def check(self, mouse_pos):
        if mouse_pos[0] > dis_left and mouse_pos[0] < dis_left + button_w and mouse_pos[1] > dis_h + 4*button_h + 4*dis_v and mouse_pos[1] < dis_h + 5*button_h + 4*dis_v:
            return True
        else:
            return False


class Button6(pygame.sprite.Sprite):
    def __init__(self):
        super(Button6, self).__init__()
        self.surf = pygame.Surface((button_w, button_h))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def check(self, mouse_pos):
        if mouse_pos[0] > dis_left and mouse_pos[0] < dis_left + button_w and mouse_pos[1] > dis_h + 5*button_h + 5*dis_v and mouse_pos[1] < dis_h + 6*button_h + 5*dis_v:
            return True
        else:
            return False

class Button_exit(pygame.sprite.Sprite):
    def __init__(self):
        super(Button_exit, self).__init__()
        self.surf = pygame.Surface((button_w, button_h))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
    def check(self, mouse_pos):
        if mouse_pos[0] > width - dis_right - button_w and mouse_pos[0] < width - dis_right and mouse_pos[1] > dis_h and mouse_pos[1] < dis_h + button_h:
            return True
        else:
            return False


class Button_star(pygame.sprite.Sprite):
    def __init__(self):
        super(Button_star, self).__init__()
        self.surf = pygame.Surface((button_w, button_h))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def check(self, mouse_pos):
        if mouse_pos[0] > width - dis_right - button_w and mouse_pos[0] < width - dis_right and mouse_pos[1] > dis_h + button_h + dis_v2 and mouse_pos[1] < dis_h + 2*button_h + dis_v2:
            return True
        else:
            return False


class Button_star1(pygame.sprite.Sprite):
    def __init__(self):
        super(Button_star1, self).__init__()
        self.surf = pygame.Surface((button_w, button_h))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def check(self, mouse_pos):
        if mouse_pos[0] > width - dis_right - button_w and mouse_pos[0] < width - dis_right and mouse_pos[1] > dis_h + 2*button_h + 2*dis_v2 and mouse_pos[1] < dis_h + 3*button_h + 2*dis_v2:
            return True
        else:
            return False


class Button_star2(pygame.sprite.Sprite):
    def __init__(self):
        super(Button_star2, self).__init__()
        self.surf = pygame.Surface((button_w, button_h))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def check(self, mouse_pos):
        if mouse_pos[0] > width - dis_right - button_w and mouse_pos[0] < width - dis_right and mouse_pos[1] > dis_h + 3*button_h + 3*dis_v2 and mouse_pos[1] < dis_h + 4*button_h + 3*dis_v2:
            return True
        else:
            return False


class Button_star3(pygame.sprite.Sprite):
    def __init__(self):
        super(Button_star3, self).__init__()
        self.surf = pygame.Surface((button_w, button_h))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def check(self, mouse_pos):
        if mouse_pos[0] > width - dis_right - button_w and mouse_pos[0] < width - dis_right and mouse_pos[1] > dis_h + 4*button_h + 4*dis_v2 and mouse_pos[1] < dis_h + 5*button_h + 4*dis_v2:
            return True
        else:
            return False



pygame.init()
pygame.display.set_caption("玩转木块")
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
running1 = True
button1 = Button1()
button2 = Button2()
button3 = Button3()
button4 = Button4()
button5 = Button5()
button6 = Button6()
button_exit = Button_exit()
button_star = Button_star()
button_star1 = Button_star1()
button_star2 = Button_star2()
button_star3 = Button_star3()
screen.fill((255, 255, 255))

COLLTYPE_BALL = 0
space = pymunk.Space()
space.gravity = 0.0, -900.0


class PhysicsDemo:
    def flipyv(self, v):
        return int(v.x), int(-v.y+self.h)

    def __init__(self):
        self.running = True
        ### Init pygame and create screen
        pygame.init()
        self.w, self.h = width, height
        self.screen = pygame.display.set_mode((self.w, self.h), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        ### Init pymunk and create space
        self.space = pm.Space()
        self.space.gravity = (0.0, -900.0)

        ### Walls
        self.walls = []
        self.create_wall_segments([(100, 50), (500, 50)])

        ## Balls
        #balls = [createBall(space, (100,300))]
        self.balls = []

        ### Polys
        self.polys = []
        h = 10
        for y in range(1, h):
            #for x in range(1, y):
            x = 0
            s = 10
            p = Vec2d(300, 40) + Vec2d(0, y*s*2)
            self.polys.append(self.create_box(p, size=s, mass=1))

        self.run_physics = True

        ### Wall under construction
        self.wall_points = []
        ### Poly under construction
        self.poly_points = []

        self.shape_to_remove = None
        self.mouse_contact = None

    def draw_helptext(self):
        font = pygame.font.Font(None, 16)
        text = ["LMB: Create ball", "LMB + Shift: Create box", "RMB on object: Remove object", "RMB(hold) + Shift: Create polygon, release to finish (we be converted to a convex hull of the points)", "RMB + Ctrl: Create wall, release to finish", "Space: Stop physics simulation", "k: Spawn a bunch of blocks", "f: Fire a ball from the top left corner", "g: Rotate the gravity"
                ]
        y = 5
        for line in text:
            text = font.render(line, 1, THECOLORS["black"])
            self.screen.blit(text, (5, y))
            y += 10

    def create_ball(self, point, mass=1.0, radius=15.0):

        moment = pm.moment_for_circle(mass, 0.0, radius)
        ball_body = pm.Body(mass, moment)
        ball_body.position = Vec2d(point)

        ball_shape = pm.Circle(ball_body, radius)
        ball_shape.friction = 1.5
        ball_shape.collision_type = COLLTYPE_DEFAULT
        self.space.add(ball_body, ball_shape)
        return ball_shape

    def create_box(self, pos, size=10, mass=5.0):
        box_points = [(-size, -size), (-size, size),
                      (size, size), (size, -size)]
        return self.create_poly(box_points, mass=mass, pos=pos)

    def create_poly(self, points, mass=5.0, pos=(0, 0)):

        moment = pm.moment_for_poly(mass, points)
        #moment = 1000
        body = pm.Body(mass, moment)
        body.position = Vec2d(pos)
        shape = pm.Poly(body, points)
        shape.friction = 0.5
        shape.collision_type = COLLTYPE_DEFAULT
        self.space.add(body, shape)
        return shape

    def create_wall_segments(self, points):
        """Create a number of wall segments connecting the points"""
        if len(points) < 2:
            return []
        points = list(map(Vec2d, points))
        for i in range(len(points)-1):
            v1 = Vec2d(points[i].x, points[i].y)
            v2 = Vec2d(points[i+1].x, points[i+1].y)
            wall_body = pm.Body(body_type=pm.Body.STATIC)
            wall_shape = pm.Segment(wall_body, v1, v2, .0)
            wall_shape.friction = 1.0
            wall_shape.collision_type = COLLTYPE_DEFAULT
            self.space.add(wall_shape)
            self.walls.append(wall_shape)

    def run(self):
        while self.running:
            self.loop()

    def draw_ball(self, ball):
        body = ball.body
        v = body.position + ball.offset.cpvrotate(body.rotation_vector)
        p = self.flipyv(v)
        r = ball.radius
        pygame.draw.circle(self.screen, THECOLORS["blue"], p, int(r), 2)

    def draw_wall(self, wall):
        body = wall.body
        pv1 = self.flipyv(
            body.position + wall.a.cpvrotate(body.rotation_vector))
        pv2 = self.flipyv(
            body.position + wall.b.cpvrotate(body.rotation_vector))
        pygame.draw.lines(self.screen, THECOLORS["black"], False, [pv1, pv2])

    def draw_poly(self, poly):
        body = poly.body
        ps = [p.rotated(body.angle) +
              body.position for p in poly.get_vertices()]
        ps.append(ps[0])
        ps = list(map(self.flipyv, ps))
        if u.is_clockwise(ps):
            color = THECOLORS["green"]
        else:
            color = THECOLORS["red"]
        pygame.draw.lines(self.screen, color, False, ps)

    def draw(self):

        ### Clear the screen
        self.screen.fill(THECOLORS["white"])

        ### Display some text
        self.draw_helptext()

        ### Draw balls
        for ball in self.balls:
            self.draw_ball(ball)

        ### Draw walls
        for wall in self.walls:
            self.draw_wall(wall)

        ### Draw polys
        for poly in self.polys:
            self.draw_poly(poly)

        ### Draw Uncompleted walls
        if len(self.wall_points) > 1:
            ps = [self.flipyv(Vec2d(p)) for p in self.wall_points]
            pygame.draw.lines(self.screen, THECOLORS["gray"], False, ps, 2)

        ### Uncompleted poly
        if len(self.poly_points) > 1:
            ps = [self.flipyv(Vec2d(p)) for p in self.poly_points]
            pygame.draw.lines(self.screen, THECOLORS["red"], False, ps, 2)

        ### Mouse Contact
        if self.mouse_contact is not None:
            p = self.flipyv(self.mouse_contact)
            pygame.draw.circle(self.screen, THECOLORS["red"], p, 3)

        ### All done, lets flip the display
        pygame.display.flip()

    def loop(self):
        global width
        global height
        global button_w
        global button_h
        global dis_left
        global dis_right
        global dis_v
        global dis_v2
        mpos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == QUIT:
                self.running = False

            elif event.type == VIDEORESIZE:
                width = event.size[0]
                height = event.size[1]
                button_w = int(width/8)
                button_h = int(height/24)
                dis_left = int(width/12)
                dis_right = int(width/24)
                dis_v = int(height/20)
                dis_h = int(height/12)
                dis_v2 = int(height/30)
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                self.running = False
            elif event.type == KEYDOWN and event.key == K_p:
                pygame.image.save(self.screen, "playground.png")

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:  # LMB
                if pygame.key.get_mods() & KMOD_SHIFT:
                    p = self.flipyv(Vec2d(event.pos))
                    self.polys.append(self.create_box(pos=p))
                else:
                    #t = -10000
                    p = self.flipyv(Vec2d(event.pos))
                    self.balls.append(self.create_ball(p))

            elif event.type == MOUSEBUTTONDOWN and event.button == 3:  # RMB
                if pygame.key.get_mods() & KMOD_SHIFT:
                    pass

                elif pygame.key.get_mods() & KMOD_CTRL:
                    p = self.flipyv(Vec2d(event.pos))
                    self.wall_points.append(p)
                elif self.shape_to_remove is not None:

                    self.balls = list(
                        filter(lambda a: a != self.shape_to_remove, self.balls))
                    self.walls = list(
                        filter(lambda a: a != self.shape_to_remove, self.walls))
                    self.polys = list(
                        filter(lambda a: a != self.shape_to_remove, self.polys))
                    self.space.remove(
                        self.shape_to_remove.body, self.shape_to_remove)

            elif event.type == KEYUP and event.key in (K_RCTRL, K_LCTRL):
                ### Create Wall
                self.create_wall_segments(self.wall_points)
                self.wall_points = []
            elif event.type == KEYUP and event.key in (K_RSHIFT, K_LSHIFT):
                ### Create Polygon

                if len(self.poly_points) > 0:
                    self.poly_points = u.reduce_poly(
                        self.poly_points, tolerance=5)
                if len(self.poly_points) > 2:
                    self.poly_points = u.convex_hull(self.poly_points)
                    if not u.is_clockwise(self.poly_points):
                        self.poly_points.reverse()

                    center = u.calc_center(self.poly_points)
                    self.poly_points = u.poly_vectors_around_center(
                        self.poly_points)
                    self.polys.append(self.create_poly(
                        self.poly_points, pos=center))
                self.poly_points = []
            elif event.type == KEYDOWN and event.key == K_SPACE:
                self.run_physics = not self.run_physics
            elif event.type == KEYDOWN and event.key == K_k:
                for x in range(-100, 100, 25):
                    for y in range(-100, 100, 25):
                        p = pygame.mouse.get_pos()
                        p = Vec2d(self.flipyv(Vec2d(p))) + (x, y)
                        self.polys.append(self.create_box(pos=p))
            elif event.type == KEYDOWN and event.key == K_b:
                p = self.flipyv(Vec2d(pygame.mouse.get_pos()))
                self.polys.append(self.create_box(p, size=10, mass=1))
            elif event.type == KEYDOWN and event.key == K_f:
                bp = Vec2d(100, 500)
                p = self.flipyv(Vec2d(pygame.mouse.get_pos())) - bp
                ball = self.create_ball(bp)
                p = p.normalized()
                ball.body.apply_impulse_at_local_point(p*1000, (0, 0))
                self.balls.append(ball)
            elif event.type == KEYDOWN and event.key == K_g:
                g = self.space.gravity
                g.rotate(45)
                self.space.gravity = g



        if pygame.key.get_mods() & KMOD_SHIFT and pygame.mouse.get_pressed()[2]:
            p = self.flipyv(Vec2d(mpos))
            self.poly_points.append(p)
        hit = self.space.point_query_nearest(
            self.flipyv(Vec2d(mpos)), 0, pm.ShapeFilter())
        if hit != None:
            self.shape_to_remove = hit.shape
        else:
            self.shape_to_remove = None

        ### Update physics
        if self.run_physics:
            x = 1
            dt = 1.0/60.0/x
            for x in range(x):
                self.space.step(dt)
                for ball in self.balls:
                    #ball.body.reset_forces()
                    pass
                for poly in self.polys:
                    #poly.body.reset_forces()
                    pass

        ### Draw stuff
        self.draw()

        ### Check for objects outside of the screen, we can remove those
        # Balls
        xs = []
        for ball in self.balls:
            if ball.body.position.x < -1000 or ball.body.position.x > 1000 \
                    or ball.body.position.y < -1000 or ball.body.position.y > 1000:
                xs.append(ball)
        for ball in xs:
            self.space.remove(ball, ball.body)
            self.balls.remove(ball)

        # Polys
        xs = []
        for poly in self.polys:
            if poly.body.position.x < -1000 or poly.body.position.x > 1000 \
                    or poly.body.position.y < -1000 or poly.body.position.y > 1000:
                xs.append(poly)

        for poly in xs:
            self.space.remove(poly, poly.body)
            self.polys.remove(poly)

        ### Tick clock and update fps in title
        self.clock.tick(50)


class set():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self):
        pygame.draw.aaline(screen, white, self.p1, self.p2, 2)  # 画出一段轨迹
        x = self.p2[0] - self.p1[0]
        y = self.p2[1] - self.p1[1]
        vec1 = Vec2d(x, y).normalized()
        vec2 = Vec2d(-y, x).normalized()
        zoom = 6
        p3 = (self.p2[0] + zoom * vec2[0], self.p2[1] + zoom * vec2[1])
        p4 = (self.p2[0] - zoom * vec2[0], self.p2[1] - zoom * vec2[1])
        p5 = (self.p2[0] + zoom * vec1[0], self.p2[1] + zoom * vec1[1])
        pygame.draw.polygon(screen, white, [p3, p4, p5], 0)


class Staic_Line:
    def __init__(self, p1, p2):
        if (p1[0] < p2[0]):
            self.p1 = Vec2d(p1[0], p1[1])
            self.p2 = Vec2d(p2[0], p2[1])
        else:
            self.p1 = Vec2d(p2[0], p2[1])
            self.p2 = Vec2d(p1[0], p1[1])
        self.vec = Vec2d(p1[0] - p2[0], p1[1] - p2[1]).normalized()
        self.k = None
        if p1[0] - p2[0] != 0:
            self.k = (p1[1] - p2[1]) / (p1[0] - p2[0])
        self.b = p1[1] - self.k * p1[0]
        self.friction = 0.5

    def draw(self):
        pygame.draw.line(screen, white, self.p1, self.p2, 5)

    def distance(self, pos):
        a = self.k * pos[0] + self.b - pos[1]
        b = sqrt(1 + self.k**2)
        return a / b


class Line:
    def __init__(self, p1, p2, w=0):
        self.p1 = p1
        self.p2 = p2
        self.mid = (0.5 * (p1[0] + p2[0]), 0.5 * (p1[1] + p2[1]))
        if(p2[0]-p1[0]):
            self.theta = math.atan((p2[1]-p1[1])/(p2[0]-p1[0]))
        else:
            self.theta = math.pi/2
        self.length = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        self.vec = Vec2d(math.cos(self.theta), math.sin(self.theta))
        self.w = w
        self.m = 100000
        self.k = 0
        self.b = 0

    def draw(self):

        pygame.draw.line(screen, white, self.p1, self.p2, 5)

    def set_beta(self):  # 角加速度
        return 0

    def update(self, ball=False):
        #while self.theta>math.pi:
        #    self.theta -= math.pi
        self.theta = self.theta + self.w
        self.w = self.w + self.set_beta()
        self.k = math.tan(self.theta)
        self.vec = Vec2d(math.cos(self.theta), math.sin(self.theta))
        if math.cos(self.theta) < 0:
            self.p1 = (self.mid[0] + (self.length / 2) * math.cos(self.theta),
                       self.mid[1] + (self.length / 2) * math.sin(self.theta))
            self.p2 = (self.mid[0] - self.length / 2 * math.cos(self.theta),
                       self.mid[1] - self.length / 2 * math.sin(self.theta))
        else:
            self.p2 = (self.mid[0] + (self.length / 2) * math.cos(self.theta),
                       self.mid[1] + (self.length / 2) * math.sin(self.theta))
            self.p1 = (self.mid[0] - self.length / 2 * math.cos(self.theta),
                       self.mid[1] - self.length / 2 * math.sin(self.theta))
        self.b = self.mid[1] - self.k * self.mid[0]
        if not ball:
            self.draw()

    def distance(self, pos):
        a = self.k * pos[0] + self.b - pos[1]
        b = sqrt(1 + self.k**2)
        return a / b

class Star():
    x, y = 0, 0  # 坐标
    vx, vy = 0, 0  # x,y方向上的速度
    ax, ay = 0, 0  # x,y方向上的加速度
    m = 0  # 质量
    r = 10  # 半径

    def __init__(self, x, y, vx, vy, m):
        self.pos = Vec2d(x, y)
        self.v = Vec2d(vx, vy)
        self.m = m
        self.r = self.calc_r()  # 半径
        self.color = (random.randint(120, 255), random.randint(120, 255),
                      random.randint(120, 255))  # 随机颜色
        self.path = []  # 轨迹坐标
        setting = set((0, 0), (0, 0))
        self.set = setting

    def calc_r(self):  # 计算星球的半径
        return int(((0.75 * self.m)**1 / 3 + 0.5) / 20)

    def set_a(self):  # 计算星球的引力加速度

        a = Vec2d(0, 0)
        for other_star in star_list:
            d_2 = other_star.pos - self.pos
            length = d_2.length
            if length != 0:
                a += (G * other_star.m * d_2) / length**3
        return a

    def update(self):  # 星球状态的刷新
        self.pos = self.pos + self.v
        self.v = self.v + self.set_a()
        if len(self.path) > max_path:
            self.path.pop(0)
        self.path.append(self.pos)
        self.draw()

    def init(self,i):  # 星球状态的刷新
        self.path.append(self.pos)
        self.draw()
        self.set.draw()
        text = [
            "velocity: " + str(Vec2d(int(self.v[0]*1000)/1000,int(self.v[1]*1000)/1000)),
            "mass: " + str(int(self.m*1000)/1000),
            "color: " + str(self.color)
        ]
        y = 60
        for line in text:
            text = font.render(line, 1, THECOLORS["white"])
            screen.blit(text, (5, i * 50+y))
            y += 15

#        screen.blit(font.render("velocity: " + str(self.v), 1, white),
#                    (0, i * 50 +40))
#        screen.blit(font.render("mass: " + str(self.m), 1, white),
#                    (0, i * 50 + 35))
#        screen.blit(font.render("color: " + str(self.color), 1, white),
#                    (0, i * 50 + 50))

    def draw(self):  # 星球及其轨迹的追踪
        pygame.draw.circle(screen, self.color,
                           (int(self.pos[0] + 0.5), int(self.pos[1] + 0.5)),
                           self.r, 2)
        len_path = len(self.path)
        for i in range(1, len_path):
            pos_a = self.path[i - 1]
            pos_b = self.path[i]
            pygame.draw.line(screen, self.color, pos_a, pos_b, 1)  # 画出一段轨迹

mouse_body = pymunk.Body(body_type = pymunk.Body.KINEMATIC)
def to_pygame(p):
    return int(p.x), int(-p.y + height)


class Ball:
    def __init__(self, r, x, y, vx, vy):
        self.r = r
        self.m = r**3
        self.pos = Vec2d(x, y)
        self.v = Vec2d(vx, vy)
        self.path = []
        self.color = (random.randint(120, 255), random.randint(120, 255),
                      random.randint(120, 255))  # 随机颜色
        self.set = set((0, 0), (0, 0))
        self.a = Vec2d(0, -g)
        self.l = Line(self.pos, self.pos + Vec2d(0, r))
        self.rotate = False
        self.collision = False

    def draw(self):  # 轨迹的追踪
        pygame.draw.circle(screen, self.color,
                           (int(self.pos[0] + 0.5), int(self.pos[1] + 0.5)),
                           int(self.r), 2)
        pygame.draw.line(
            screen, white, self.pos,
            Vec2d(self.pos[0] + self.r * math.cos(self.l.theta),
                  self.pos[1] + self.r * math.sin(self.l.theta)), 1)
        len_path = len(self.path)
        for i in range(1, len_path):
            pos_a = self.path[i - 1]
            pos_b = self.path[i]
            pygame.draw.aaline(screen, self.color, pos_a, pos_b, 1)  # 画出一段轨迹

    def update(self):  # 运动状态的刷新

        change = False
        ground_friction = 0.8
        if self.pos[0] > width - self.r:
            self.v[0] = -0.8 * self.v[0]
            self.pos[0] = width - self.r
            change = True
            self.collision = True
        elif self.pos[0] < self.r:
            self.v[0] = -0.8 * self.v[0]
            self.pos[0] = self.r
            change = True
            self.collision = True
        if self.pos[1] > height - self.r:
            self.v[1] = -0.8 * self.v[1]
            self.pos[1] = height - self.r
            change = True
            self.collision = True
        elif self.pos[1] < self.r:
            self.v[1] = -0.8 * self.v[1]
            self.pos[1] = self.r
            change = True
            self.collision = True
        else:
            self.collision = False
        if self.rotate:
            self.l.w = self.v.length / self.r * 0.5
        if not change:
            self.pos = self.pos + self.v
            self.v = self.v + self.a
        else:
            if self.v[0] != 0:
                self.rotate = True
        self.l.update(True)
        if len(self.path) > max_path:
            self.path.pop(0)
        self.path.append(self.pos)
        self.draw()

    def check(self):
        if self.pos[0] < width - self.r and self.pos[0] > self.r and self.pos[
                1] < height - self.r and self.pos[1] > self.r:
            return False
        else:
            return True

    def init(self, pos, i):  # 星球状态的刷新

        self.path.append(self.pos)
        self.draw()
        self.set.draw()
        if (pos - self.pos).length <= self.r:
            self.r = self.r + 0.1
            self.m = self.r**3
        screen.blit(font.render("velocity: " + str(Vec2d(int(self.v[0]*1000)/1000,int(self.v[1]*1000)/1000)), 1, white),
                    (0, i * 50 + 20))
        screen.blit(font.render("mass: " + str(int(self.m*1000)/1000), 1, white),
                    (0, i * 50 + 35))
        screen.blit(font.render("color: " + str(self.color), 1, white),
                    (0, i * 50 + 50))


def update():
    len1 = len(ball_list)
    len2 = len(line_list)
    len3 = len(lines)
    collide_event_list = []
    for i in range(len1):
        collide = 0  # 碰撞次数
        collide_list = []

        if not initialize:
            flag=False
            ball_list[i].update()
            for m in range(len1):
                if i == m:
                    continue
                dis = (ball_list[m].pos - ball_list[i].pos).length
                if dis <= ball_list[i].r + ball_list[m].r :
                    #if len(ball_list[m].path)>1 and len(ball_list[i].path)>1 and (ball_list[m].path[-2] - ball_list[i].path[-2]).length > ball_list[i].r + ball_list[m].r:
                    pos = ball_list[m].pos - ball_list[i].pos
                    pos = pos.normalized()
                    #ball_list[m].pos = pos * ball_list[m].r + ball_list[i].pos
                    pos_vt = -Vec2d(pos[1], -pos[0])
                    v0 = ball_list[m].v.dot(pos) * pos
                    v1 = ball_list[i].v.dot(pos) * pos
                    if (v0 - v1).dot(pos) < 0:
                        collide_event_list.append((i, m))
                        flag=True
                        v0_vt = ball_list[m].v.dot(pos_vt) * pos_vt
                        v1_vt = ball_list[i].v.dot(pos_vt) * pos_vt  # 垂直球心连线
                        k = ball_list[m].m + ball_list[i].m
                        k0 = ball_list[m].m * v0 + ball_list[i].m * v1
                        k1 = e * ball_list[m].m * (v1 - v0)
                        k2 = e * ball_list[i].m * (v0 - v1)
                        v0, v1 = (k0 + k1) / k, (k0 + k2) / k
                        ball_list[m].v = v0 + v0_vt
                        ball_list[i].v = v1 + v1_vt
                        collide += 1
                        #ball_list[m].collision=True
                        #ball_list[i].collision=True
            #if flag:
            #    ball_list[i].a=Vec2d(0,0)
            #if
            #if (ball_list[m].path[-3] - ball_list[i].path[-3]).length <= ball_list[i].r + ball_list[m].r:
            #    ball_list[m].a.dot(ball_list[m].pos - ball_list[i].pos)



            for j in range(len2):
                dis = line_list[j].distance(ball_list[i].pos)

                if ball_list[i].r + 1 >= (
                        line_list[j].p1 - ball_list[i].pos).length and (
                            line_list[j].p1 - ball_list[i].pos).dot(
                                ball_list[i].v) > 0 and Vec2d(1,line_list[j].k).dot(ball_list[i].v) > 0:

                    vec = (line_list[j].p1 - ball_list[i].pos).normalized()
                    vec_vt = Vec2d(-vec[1], vec[0])
                    vy = -vec.dot(ball_list[i].v) * vec
                    vx = -vec_vt.dot(ball_list[i].v) * vec_vt
                    if len(ball_list[i].path) > 1 and (
                            line_list[j].p1 -
                            ball_list[i].path[-2]).length <= ball_list[i].r:
                        vy = -vy
                    ball_list[i].v = vx + vy
                    collide = collide + 1
                    collide_list.append(j)
                    ball_list[i].collision = True
                elif ball_list[i].r + 1 >= (
                        line_list[j].p2 - ball_list[i].pos).length and (
                            line_list[j].p2 - ball_list[i].pos).dot(
                                ball_list[i].v) > 0 and Vec2d(1,line_list[j].k).dot(ball_list[i].v) < 0:
                    vec = (p2 - ball_list[i].pos).normalized()
                    vec_vt = Vec2d(-vec[1], vec[0])
                    vy = -vec.dot(ball_list[i].v) * vec
                    vx = -vec_vt.dot(ball_list[i].v) * vec_vt
                    if len(ball_list[i].path) > 1 and (
                            line_list[j].p2 -
                            ball_list[i].path[-2]).length <= ball_list[i].r:
                        vy = -vy

                    ball_list[i].v = vx + vy
                    collide = collide + 1
                    collide_list.append(j)
                    ball_list[i].collision = True
                elif ball_list[i].r + 1 >= abs(dis):
                    ball_list[i].rotate = True
                    if (line_list[j].p1 - ball_list[i].pos).dot(
                                Vec2d(1, line_list[j].k)) > 0:  # 延长线
                        continue
                    elif (line_list[j].p2 - ball_list[i].pos).dot(
                            Vec2d(1, line_list[j].k)) < 0:
                        continue
                    if len(ball_list[i].path) >= 2 and abs(
                        line_list[j].distance(
                            ball_list[i].path[-2])) <= ball_list[i].r-2:

                        k1 = line_list[j].k
                        v1=Vec2d( 1 / sqrt(1 + k1**2), k1/ sqrt(
                            1 + k1**2))
                        v2=Vec2d( -k1/ sqrt(1 + k1**2),  1/ sqrt(
                            1 + k1**2))
                        v3=v2*(ball_list[i].r-abs(dis))
                        pos1=ball_list[i].pos.dot(v1)*v1
                        pos2=ball_list[i].pos.dot(v2)*v2
                        if dis>0:
                            ball_list[i].pos=pos1+pos2-v3
                        else:
                            ball_list[i].pos=pos1+pos2+v3
                    if dis > 0:
                        k1 = line_list[j].k
                        ball_list[i].a = ball_list[i].a.dot(Vec2d(k1 / sqrt(1 + k1**2), 1 / sqrt(
                            1 + k1**2)))*Vec2d(k1 / sqrt(1 + k1**2), 1 / sqrt(1 + k1**2))
                    ball_list[i].collision = True
                    vx = line_list[j].vec.dot(
                        ball_list[i].v) * line_list[j].vec
                    vec = Vec2d(-line_list[j].vec[1], line_list[j].vec[0])
                    vy = -e * vec.dot(ball_list[i].v) * vec
                    if len(ball_list[i].path) >= 2 and abs(
                        line_list[j].distance(
                            ball_list[i].path[-2])) <= ball_list[i].r:
                        vy = -vy
                    ball_list[i].v = vx + vy
                    collide = collide + 1
                    collide_list.append(j)
                else:
                    ball_list[i].collision = False
                    ball_list[i].a=Vec2d(0,-g)

        else:
            ball_list[i].init(
                Vec2d(pygame.mouse.get_pos()[0],
                      pygame.mouse.get_pos()[1]), i)

        if collide >= 2:
            ball_list[i].rotate = False
            ball_list[i].w = 0
            collide_list = list(itertools.permutations(collide_list, 2))
            for index in collide_list:
                vec1 = Vec2d(1, line_list[index[0]].k)
                vec2 = Vec2d(1, line_list[index[1]].k)
                if vec1.dot(vec2) > 0:
                    ball_list[i].v = Vec2d(0, 0)
        elif collide == 1 and ball_list[i].check():
            ball_list[i].v = Vec2d(0, 0)
            ball_list[i].rotate = False
            ball_list[i].l.w = 0
        for k in range(len3):
            dis = lines[k].distance(ball_list[i].pos)
            if ball_list[i].r>= (lines[k].p1 - ball_list[i].pos).length and (lines[k].p1 - ball_list[i].pos).dot(Vec2d(1, lines[k].k)) > 0:
                if (lines[k].p1 - ball_list[i].pos).dot(
                        ball_list[i].v) < 0:
                    continue
                vec = (p1 - ball_list[i].pos).normalized()
                vec_vt = Vec2d(-vec[1], vec[0])
                vy = -vec.dot(ball_list[i].v) * vec
                vx = vec_vt.dot(ball_list[i].v) * vec_vt
                if len(ball_list[i].path) > 1 and (lines[k].p1 - ball_list[i].path[-2]).length <= ball_list[i].r:
                    vy = -vy
                ball_list[i].v = vx + vy
                collide = collide + 1
                collide_list.append(j)
                ball_list[i].collision = True
            elif ball_list[i].r >= (
                    lines[k].p2 - ball_list[i].pos).length and (lines[k].p2 - ball_list[i].pos).dot(Vec2d(1, lines[k].k)) < 0:
                if (lines[k].p2 - ball_list[i].pos).dot(
                        ball_list[i].v) < 0:
                    continue
                vec = (p2 - ball_list[i].pos).normalized()
                vec_vt = Vec2d(-vec[1], vec[0])
                vy = -vec.dot(ball_list[i].v) * vec
                vx = vec_vt.dot(ball_list[i].v) * vec_vt
                if len(ball_list[i].path) > 1 and (
                        lines[k].p2 -
                        ball_list[i].path[-2]).length <= ball_list[i].r:
                    vy = -vy
                ball_list[i].v = vx + vy
                collide = collide + 1
                collide_list.append(j)
                ball_list[i].collision = True
            elif ball_list[i].r >= abs(dis):
                if (lines[k].p1 - ball_list[i].pos).dot(Vec2d(1, lines[k].k)) * (lines[k].p2 - ball_list[i].pos).dot(Vec2d(1, lines[k].k)) > 0:  # 延长线
                    continue
                k1 = lines[k].k
                ball_list[i].a = ball_list[i].a.dot(
                    Vec2d(k1 / sqrt(1 + k1**2), 1 / sqrt(1 + k1**2)))*Vec2d(k1 / sqrt(1 + k1**2), 1 / sqrt(1 + k1**2))
                if dis > 0:
                    if len(ball_list[i].path) >= 15 and ball_list[i].r > lines[k].distance(ball_list[i].path[-15]):
                        ball_list[i].v = ball_list[i].v.dot(
                            Vec2d(k1 / sqrt(1 + k1**2),
                                  1 / sqrt(1 + k1**2))) * Vec2d(
                            k1 / sqrt(1 + k1**2), 1 / sqrt(1 + k1**2))

                ball_list[i].rotate = True
                k1 = lines[k].k
                ball_list[i].collision = True
                v1 = ball_list[i].v.dot(
                    Vec2d(-math.sin(lines[k].theta), math.cos(lines[k].theta)))*Vec2d(-math.sin(lines[k].theta), math.cos(lines[k].theta))
                v2 = ball_list[i].v.dot(
                    Vec2d(1 / sqrt(1 + k1**2), k1 / sqrt(1 + k1**2)))*Vec2d(k1 / sqrt(1 + k1**2), 1 / sqrt(1 + k1**2))
                x = (ball_list[i].pos - lines[k].mid).dot(
                    Vec2d(math.cos(lines[k].theta), math.sin(lines[k].theta)))
                v3 = lines[k].w * abs(x)*0.01 * \
                    Vec2d(-math.sin(lines[k].theta), math.cos(lines[k].theta))

                lines[k].w = (v1.length-v3.length)*0.01
                if ball_list[i].pos[0] < lines[k].mid[0] and dis > 0:
                    lines[k].w = -lines[k].w
                elif ball_list[i].pos[0] > lines[k].mid[0] and dis < 0:
                    lines[k].w = -lines[k].w
                ball_list[i].v = v2-v1+v3
            else:
                ball_list[i].a = Vec2d(0, -g)
            for j in range(len2):
                if lines[k].distance(line_list[j].p1)*lines[k].distance(line_list[j].p2)<=0:
                    if line_list[j].distance(lines[k].p1)*line_list[j].distance(lines[k].p2)<=0:
                        lines[k].w=-lines[k].w

    for index in collide_event_list:
        pos=(ball_list[index[0]].pos-ball_list[index[1]].pos).normalized()*(ball_list[index[0]].r+ball_list[index[1]].r)
        if index[0] == index[1]:
            continue
        if ball_list[index[0]].collision and ball_list[index[1]].collision:
            ball_list[index[0]].pos = pos + ball_list[index[1]].pos
            ball_list[index[1]].pos = -pos + ball_list[index[0]].pos
            continue
        if ball_list[index[1]].collision:
            ball_list[index[0]].pos = pos + ball_list[index[1]].pos
            continue
        if ball_list[index[0]].collision:
            ball_list[index[1]].pos = -pos + ball_list[index[0]].pos
            continue
    collide_event_list = []
    for line in lines:
        line.update()


def check_collision():

    collide_event_list = []

    # 用于循环的临时列表，处理后的死星将会设为-1，跳过当前循环
    for i in range(len(ball_list)):
        for j in range(len(ball_list)):
            if i == j:
                continue  # 开始统计单次事件中的碰撞星体
            dis = (ball_list[j].pos - ball_list[i].pos).length
            if dis <= ball_list[j].r + ball_list[j].r:  # 如果发生碰撞
                collide_event_list.append((i, j))
    for i in range(len(collide_event_list)):
        for j in range(len(collide_event_list)):
            if i == j:
                continue  # 开始统计单次事件中的碰撞星体
            if collide_event_list[i][0] == collide_event_list[j][
                    0] and collide_event_list[i][1] == collide_event_list[j][
                        1]:  # 如果发生碰撞
                collide_event_list[j] = (-1, -1)
            elif collide_event_list[i][1] == collide_event_list[j][
                    0] and collide_event_list[i][0] == collide_event_list[j][1]:
                collide_event_list[j] = (-1, -1)
    return collide_event_list  # 返回菜单目录和菜单



#for i in range(6):
#    for j in range(5):
#        lines.append(Line( (i*114,30+j*80), (i*114+70,30+j*80)))
#for i in range(3):
#    for j in range(1):
#        lines.append(Line( (i*137.5,50+150*j), (i*137.5+90,50+150*j)))



X,Y = 0, 1
COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL1 = 2
def flipy(y):
    return -y + height
def mouse_coll_func(arbiter, space, data):
    s1, s2 = arbiter.shapes
    s2.unsafe_set_radius(s2.radius + 0.15)
    return False
mouse_shape = pymunk.Circle(mouse_body, 3, (0, 0))
mouse_shape.collision_type = COLLTYPE_MOUSE
space.add(mouse_shape)
space.add_collision_handler(COLLTYPE_MOUSE, COLLTYPE_BALL1).pre_solve = mouse_coll_func
line_point1 = None
static_lines = []
run_physics = True


class Ball2:
    def __init__(self, r, x, y, dx, dy):
        self.r = r
        self.color = (random.randint(0, 250), random.randint(
            0, 250), random.randint(0, 250))
        self.position = Vec2d(x, y)
        self.position1 = Vec2d(x, y)
        #self.v = Vec2d(dx, dy)
        #self.a = Vec2d(0, 0)
        #self.a1 = Vec2d(0, 0)
        #self.a2 = Vec2d(0, 0)
        self.set = set((0, 0), (0, 0))
        self.own = Vec2d(mid, 0)
        #print(self.position)
        self.theta0 = acos((self.position - self.own) .dot(Vec2d(1, 0)) /
                           (self.position - self.own).length) - pi * 0.5
        self.theta = 0
        self.t = 0
        #self.alpha = (-1) * acos((self.position - self.own) .dot(Vec2d(1, 0)) / (self.position - self.own).length) + pi
        self.path = []

    def exist(self):
        pygame.draw.circle(screen, self.color, (int(
            self.position1[0] + 0.5), int(self.position1[1] + 0.5)), self.r, 0)

    def update(self):
        self.theta = self.theta0 * \
            cos(sqrt(2 * pi * (self.position - self.own).length) * self.t)
        self.position1 = ((-1) * (self.position - self.own).length * sin(
            self.theta) + mid, (self.position - self.own).length * cos(self.theta))
        self.t = self.t + 1 / (20*fps)
        if self.t == 1:
            self.t = 0
        #print((self.position - self.own).dot(Vec2d(1, 0)))
        #print((self.position - self.own).length)
        #print(self.theta)
        #self.a1 = Vec2d(g * cos(self.theta) * sin(self.theta), g * cos(self.theta) * cos(self.theta))
        #self.a2 = Vec2d(2 * g * (sin(self.theta) - sin(self.alpha)) * cos(self.theta), (-1) * 2 * g * (sin(self.theta) - sin(self.alpha)) * sin(self.theta))
        #self.a = self.a1 + self.a2
        #print(self.a1)
        #print(self.a2)
        #self.position = self.position + self.v
        #self.v = self.v + self.a  #在这里考虑轨迹方程，此处路径计算有错
        self.path.append(self.position1)
        pygame.draw.circle(screen, self.color, (int(
            self.position1[0] + 0.5), int(self.position1[1] + 0.5)), self.r, 0)

    def init(self):
        self.path.append(self.position1)
        self.draw()
        self.set.draw()


class Line2:
    def __init__(self, x, y):
        self.position = Vec2d(x, y)
        self.position1 = Vec2d(x, y)
        self.own = Vec2d(mid, 0)
        self.path = []
        self.theta0 = acos((self.position - self.own).dot(Vec2d(1, 0)) /
                           (self.position - self.own).length) - pi * 0.5
        self.theta = 0
        self.t = 0

    def exist(self):
        pygame.draw.line(screen, white, self.position1, (mid, 0), 1)

    def update(self):
        self.theta0 = acos((self.position - self.own).dot(Vec2d(1, 0)) /
                           (self.position - self.own).length) - pi * 0.5
        self.theta = self.theta0 * \
            cos(sqrt(2 * pi * (self.position - self.own).length) * self.t)
        self.position1 = ((-1) * (self.position - self.own).length * sin(self.theta) + mid,
                          (self.position - self.own).length * cos(self.theta))
        self.t = self.t + 1 / (20 * fps)
        if self.t == 1:
            self.t = 0
        self.path.append(self.position1)
        pygame.draw.line(screen, white, self.position1, (mid, 0), 1)

    def init(self):
        self.path.append(self.position1)
        self.draw()
        self.set.draw()

while running:
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(background_size, (0, 0))
    screen.blit(button1.surf, (dis_left, dis_h))
    screen.blit(model1_size, (dis_left, dis_h))
    screen.blit(button2.surf, (dis_left, dis_h + button_h + dis_v))
    screen.blit(model2_size, (dis_left, dis_h + button_h + dis_v))
    screen.blit(button3.surf, (dis_left, dis_h + 2*button_h + 2*dis_v))
    screen.blit(model3_size, (dis_left, dis_h + 2*button_h + 2*dis_v))
    screen.blit(button4.surf, (dis_left, dis_h + 3*button_h + 3*dis_v))
    screen.blit(model4_size, (dis_left, dis_h + 3*button_h + 3*dis_v))
    screen.blit(button5.surf, (dis_left, dis_h + 4*button_h + 4*dis_v))
    screen.blit(model5_size, (dis_left, dis_h + 4*button_h + 4*dis_v))
    screen.blit(button6.surf, (dis_left, dis_h + 5*button_h + 5*dis_v))
    screen.blit(model6_size, (dis_left, dis_h + 5*button_h + 5*dis_v))
    button1.surf = pygame.Surface((button_w, button_h))
    button2.surf = pygame.Surface((button_w, button_h))
    button3.surf = pygame.Surface((button_w, button_h))
    button4.surf = pygame.Surface((button_w, button_h))
    button5.surf = pygame.Surface((button_w, button_h))
    button6.surf = pygame.Surface((button_w, button_h))


    if button1.check(mouse_pos) == True:
        button1.surf.fill((255, 0, 0))
    else:
        button1.surf.fill((0, 0, 0))
    if button2.check(mouse_pos) == True:
        button2.surf.fill((255, 0, 0))
    else:
        button2.surf.fill((0, 0, 0))
    if button3.check(mouse_pos) == True:
        button3.surf.fill((255, 0, 0))
    else:
        button3.surf.fill((0, 0, 0))
    if button4.check(mouse_pos) == True:
        button4.surf.fill((255, 0, 0))
    else:
        button4.surf.fill((0, 0, 0))
    if button5.check(mouse_pos) == True:
        button5.surf.fill((255, 0, 0))
    else:
        button5.surf.fill((0, 0, 0))
    if button6.check(mouse_pos) == True:
        button6.surf.fill((255, 0, 0))
    else:
        button6.surf.fill((0, 0, 0))

    background_size = pygame.transform.scale(background, (width, height))
    model1_size = pygame.transform.scale(model1, (button_w, button_h))
    model2_size = pygame.transform.scale(model2, (button_w, button_h))
    model3_size = pygame.transform.scale(model3, (button_w, button_h))
    model4_size = pygame.transform.scale(model4, (button_w, button_h))
    model5_size = pygame.transform.scale(model5, (button_w, button_h))
    model6_size = pygame.transform.scale(model6, (button_w, button_h))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == VIDEORESIZE:
            width = event.size[0]
            height = event.size[1]
            button_w = int(width/8)
            button_h = int(height/24)
            dis_left = int(width/12)
            dis_right = int(width/24)
            dis_v = int(height/20)
            dis_h = int(height/12)
            dis_v2 = int(height/30)
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        elif event.type == MOUSEBUTTONDOWN:
            balls=[]
            length = 125
            if button1.check(mouse_pos) == True:
                draw_options = pymunk.pygame_util.DrawOptions(screen)
                balls=[]
                #小球初始化和约束节点的生成
                for x in range(100,width-200,50):
                    mass=10
                    ball_radius=25
                    moment = pymunk.moment_for_circle(mass, 0, ball_radius, (0, 0))
                    ball_body = pymunk.Body(mass, moment)
                    ball_body.position=(x,300)
                    ball_shape = pymunk.Circle(ball_body, ball_radius)
                    ball_shape.elasticity = 0.99
                    space.add(ball_body, ball_shape)
                    balls.append(ball_shape)
                    PinJoint = pymunk.PinJoint(space.static_body, ball_body, (ball_body.position[0], length+ball_body.position[1]), (0, 0))
                    space.add(PinJoint)

    #鼠标对象的生成
                mouse_joint = None
                mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
                running1 = True
                button1.surf.fill((255, 255, 255))
                screen.blit(button1.surf, (50, 55))

                while running ==True and running1 == True:
                    mouse_body.position =pygame.mouse.get_pos()[0],height-pygame.mouse.get_pos()[1]
                    mouse_pos = pygame.mouse.get_pos()
                    screen.fill((255, 255, 255))

                    screen.blit(button_exit.surf, (width - dis_right - button_w, dis_h))
                    screen.blit(
                        back_size, (width - dis_right - button_w, dis_h))
                    back_size = pygame.transform.scale(
                        back, (button_w, button_h))
                    button_exit.surf = pygame.Surface((button_w, button_h))
                    if button_exit.check(mouse_pos) == True:
                        button_exit.surf.fill((255, 0, 0))
                    else:
                        button_exit.surf.fill((0, 0, 0))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            running = False
                        elif event.type == VIDEORESIZE:
                            width = event.size[0]
                            height = event.size[1]
                            button_w = int(width/8)
                            button_h = int(height/24)
                            dis_left = int(width/12)
                            dis_right = int(width/24)
                            dis_v = int(height/20)
                            dis_h = int(height/12)
                            dis_v2 = int(height/30)
                            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                        elif event.type == MOUSEBUTTONDOWN:
                            if button_exit.check(mouse_pos) == True:
                                running1 = False
                                for ball in balls:
                                    space.remove(ball)
                                    space.remove(ball.body)
                                for c in space.constraints:
                                    space.remove(c)
                            if mouse_joint != None:
                                space.remove(mouse_joint)
                                mouse_joint = None
                            p = Vec2d(event.pos)
                            hit = space.point_query_nearest(p, 5, pymunk.ShapeFilter())
                            if hit != None and hit.shape.body.body_type == pymunk.Body.DYNAMIC:
                                shape = hit.shape
                                if hit.distance > 0:
                                    nearest = hit.point
                                else:
                                    nearest = p
                                    mouse_joint = pymunk.PivotJoint(mouse_body, shape.body, (0,0), shape.body.world_to_local(nearest))
                                    mouse_joint.max_force = 50000
                                    mouse_joint.error_bias = (1-0.15) ** 60
                                    space.add(mouse_joint)
                        elif event.type == MOUSEBUTTONUP:
                            if mouse_joint != None:
                                space.remove(mouse_joint)
                                mouse_joint = None
                    for ball in balls:
                        pos = to_pygame(ball.body.position)
                        pygame.draw.circle(screen, (255, 0, 0), pos, 25, 0)
                    for c in space.constraints:
                        pv1 = c.a.position + c.anchor_a
                        pv2 = c.b.position + c.anchor_b
                        p1 = to_pygame(pv1)
                        p2 = to_pygame(pv2)
                        pygame.draw.aalines(screen, (0, 0, 0), False, [p1, p2])
                    font = pygame.font.Font(None, 16)
                    screen.blit(font.render("Drag the ball with the left mouse button", 1, (255, 255, 255)), (0, 0))
                    space.debug_draw(draw_options)
                    fps = 60
                    dt = 1./fps
                    space.step(dt)
                    clock.tick(fps)
                    if running1 == False:
                        screen.fill((255, 255, 255))
                    pygame.display.flip()




            elif button2.check(mouse_pos) == True:
                balls = []
                running1 = True
                button2.surf.fill((255, 255, 255))
                screen.blit(button2.surf, (50, 110))
                X,Y = 0, 1
                COLLTYPE_DEFAULT = 0
                COLLTYPE_MOUSE = 1
                COLLTYPE_BALL1 = 2
                mouse_shape = pymunk.Circle(mouse_body, 3, (0, 0))
                mouse_shape.collision_type = COLLTYPE_MOUSE
                space.add(mouse_shape)
                space.add_collision_handler(COLLTYPE_MOUSE, COLLTYPE_BALL1).pre_solve = mouse_coll_func
                line_point1 = None
                static_lines = []
                run_physics = True
                while running == True and running1 == True:
                    mouse_pos = pygame.mouse.get_pos()
                    screen.fill((255, 255, 255))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            running = False
                        elif event.type == VIDEORESIZE:
                            width = event.size[0]
                            height = event.size[1]
                            button_w = int(width/8)
                            button_h = int(height/24)
                            dis_left = int(width/12)
                            dis_right = int(width/24)
                            dis_v = int(height/20)
                            dis_h = int(height/12)
                            dis_v2 = int(height/30)
                            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                        elif event.type == MOUSEBUTTONDOWN:
                            if button_exit.check(mouse_pos) == True:
                                running1 = False
                                for ball in balls:
                                    space.remove(ball)
                                    space.remove(ball.body)
                                for line in static_lines:
                                    space.remove(line)
                            if event.button == 1 and button_exit.check(mouse_pos) == False:
                                p = event.pos[X], flipy(event.pos[Y])
                                body = pymunk.Body(10, 100)
                                body.position = p
                                shape = pymunk.Circle(body, 10, (0, 0))
                                shape.friction = 0.5
                                shape.collision_type = COLLTYPE_BALL1
                                space.add(body, shape)
                                balls.append(shape)
                            if event.button == 3:  # 画线斜面
                                if line_point1 is None:
                                    line_point1 = Vec2d(event.pos[X], flipy(event.pos[Y]))
                        elif event.type == MOUSEBUTTONUP and event.button == 3:
                            if line_point1 is not None:
                                line_point2 = Vec2d(event.pos[X], flipy(event.pos[Y]))
                                body = pymunk.Body(body_type=pymunk.Body.STATIC)
                                shape = pymunk.Segment(body, line_point1, line_point2, 0.0)
                                shape.friction = 0.99
                                space.add(shape)
                                static_lines.append(shape)
                                line_point1 = None
                        elif event.type == KEYDOWN and event.key == K_SPACE:
                            run_physics = not run_physics
                    p = pygame.mouse.get_pos()  # 获得鼠标光标的位置
                    mouse_pos1 = Vec2d(p[X], flipy(p[Y]))
                    mouse_body.position = mouse_pos1
                    if pygame.key.get_mods() & KMOD_SHIFT and pygame.mouse.get_pressed()[0]:
                        body = pymunk.Body(10, 10)
                        body.position = mouse_pos1
                        shape = pymunk.Circle(body, 10, (0, 0))
                        shape.collision_type = COLLTYPE_BALL
                        space.add(body, shape)
                        balls.append(shape)

        ### Update physics
                    if run_physics:
                        dt = 1.0/60.0
                        for x in range(1):
                            space.step(dt)

        ### Draw stuff
                    screen.fill(THECOLORS["white"])

                    # Display some text
                    font = pygame.font.Font(None, 16)
                    text = """LMB: Create ball
            LMB + Shift: Create many balls
            RMB: Drag to create wall, release to finish
            Space: Pause physics simulation"""
                    y = 5
                    for line in text.splitlines():
                        text = font.render(line, 1, THECOLORS["black"])
                        screen.blit(text, (5, y))
                        y += 10

                    for ball in balls:
                        r = ball.radius
                        v = ball.body.position
                        rot = ball.body.rotation_vector
                        p = int(v.x), int(flipy(v.y))
                        p2 = Vec2d(rot.x, -rot.y) * r * 0.9
                        pygame.draw.circle(screen, THECOLORS["blue"], p, int(r), 2)
                        pygame.draw.line(screen, THECOLORS["red"], p, p+p2)

                    if line_point1 is not None:
                        p1 = line_point1.x, flipy(line_point1.y)
                        p2 = mouse_pos1.x, flipy(mouse_pos1.y)
                        pygame.draw.lines(screen, THECOLORS["black"], False, [p1, p2])

                    for line in static_lines:
                        body = line.body

                        pv1 = body.position + line.a.rotated(body.angle)
                        pv2 = body.position + line.b.rotated(body.angle)
                        p1 = pv1.x, flipy(pv1.y)
                        p2 = pv2.x, flipy(pv2.y)
                        pygame.draw.lines(screen, (0, 0, 0), False, [p1,p2])
                    if running1 == False:
                        screen.fill((255, 255, 255))

                    screen.blit(button_exit.surf,
                                (width - dis_right - button_w, dis_h))
                    screen.blit(
                        back_size, (width - dis_right - button_w, dis_h))
                    back_size = pygame.transform.scale(
                        back, (button_w, button_h))
                    button_exit.surf = pygame.Surface((button_w, button_h))

                    if button_exit.check(mouse_pos) == True:
                        button_exit.surf.fill((255, 0, 0))
                    else:
                        button_exit.surf.fill((0, 0, 0))
                    pygame.display.flip()
                    clock.tick(50)


            elif button3.check(mouse_pos) == True:
                G = 0.08  # 万有引力常量
                FPS = 60  # 帧数
                exact = 50  # 每帧计算几次
                font = pygame.font.SysFont("Arial", 16)
                max_path = 500
                density = 1  # 密度
                star_list = []  # 星球列表
                set_list = []
                black = (0, 0, 0)
                white = (255, 255, 255)
                time_step = 5
                running1 = True
                button3.surf.fill((255, 255, 255))
                screen.blit(button3.surf, (50, 110))
                p1, p2 = (0, 0), (0, 0)
                initialize = True
                while running == True and running1 == True:
                    mouse_pos = pygame.mouse.get_pos()
                    screen.fill((0, 0, 0))
                    text = [
                        "Click the right mouse button and drag your mouse to generate the ball and v",
                        "press Space to start stimulation",
                        "press R to reset "
                    ]
                    y = 5
                    for line in text:
                        text = font.render(line, 1, THECOLORS["white"])
                        screen.blit(text, (0, y))
                        y += 15

                    screen.blit(button_exit.surf,
                                (width - dis_right - button_w, dis_h))
                    screen.blit(
                        back_size, (width - dis_right - button_w, dis_h))
                    back_size = pygame.transform.scale(
                        back, (button_w, button_h))

                    screen.blit(button_star.surf,
                                (width - dis_right - button_w, dis_h + button_h + dis_v2))
                    screen.blit(threestars_size,
                                (width - dis_right - button_w, dis_h + button_h + dis_v2))
                    screen.blit(button_star1.surf,
                                (width - dis_right - button_w, dis_h + 2*button_h + 2*dis_v2))
                    screen.blit(threestars2_size,
                                (width - dis_right - button_w, dis_h + 2*button_h + 2*dis_v2))
                    screen.blit(button_star2.surf,
                                (width - dis_right - button_w, dis_h + 3*button_h + 3*dis_v2))
                    screen.blit(fourstars2_size,
                                (width - dis_right - button_w, dis_h + 3*button_h + 3*dis_v2))
                    screen.blit(button_star3.surf,
                                (width - dis_right - button_w, dis_h + 4*button_h + 4*dis_v2))
                    screen.blit(fourstars_size,
                                (width - dis_right - button_w, dis_h + 4*button_h + 4*dis_v2))
                    fourstars_size = pygame.transform.scale(
                        fourstars, (button_w, button_h))
                    threestars_size = pygame.transform.scale(
                        threestars, (button_w, button_h))
                    fourstars2_size = pygame.transform.scale(
                        fourstars2, (button_w, button_h))
                    threestars2_size = pygame.transform.scale(
                        threestars2, (button_w, button_h))
                    button_exit.surf = pygame.Surface((button_w, button_h))
                    button_star1.surf = pygame.Surface((button_w, button_h))
                    button_star.surf = pygame.Surface((button_w, button_h))
                    button_star2.surf = pygame.Surface((button_w, button_h))
                    button_star3.surf = pygame.Surface((button_w, button_h))
                    if button_exit.check(mouse_pos) == True:
                        button_exit.surf.fill((255, 0, 0))
                    else:
                        button_exit.surf.fill((0, 0, 0))
                    if button_star.check(mouse_pos) == True:
                        button_star.surf.fill((255, 0, 0))
                    else:
                        button_star.surf.fill((0, 0, 0))
                    if button_star1.check(mouse_pos) == True:
                        button_star1.surf.fill((255, 0, 0))
                    else:
                        button_star1.surf.fill((0, 0, 0))
                    if button_star2.check(mouse_pos) == True:
                        button_star2.surf.fill((255, 0, 0))
                    else:
                        button_star2.surf.fill((0, 0, 0))
                    if button_star3.check(mouse_pos) == True:
                        button_star3.surf.fill((255, 0, 0))
                    else:
                        button_star3.surf.fill((0, 0, 0))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            running = False
                        elif event.type == VIDEORESIZE:
                            width = event.size[0]
                            height = event.size[1]
                            button_w = int(width/8)
                            button_h = int(height/24)
                            dis_left = int(width/12)
                            dis_right = int(width/24)
                            dis_v = int(height/20)
                            dis_h = int(height/12)
                            dis_v2 = int(height/30)
                            screen = pygame.display.set_mode(
                                (width, height), pygame.RESIZABLE)
                        elif event.type == MOUSEBUTTONDOWN:
                            if button_exit.check(mouse_pos) == True:
                                running1 = False
                            if button_star.check(mouse_pos) == True:
                                star_list.append(Star(200, 300, 0, 0.8, 1000))
                                star_list.append(Star(400, 300, 0, -0.8, 1000))
                                star_list.append(Star(300, 300, 0, 0, 1000))

                            if button_star1.check(mouse_pos) == True:
                                star_list.append(
                                    Star(200, 300, -0.3, -math.sqrt(3)*0.3, 1000))
                                star_list.append(
                                    Star(400, 300, -0.3, math.sqrt(3)*0.3, 1000))
                                star_list.append(
                                    Star(300, 300-math.sqrt(3)*100, 0.6, 0, 1000))
                            if button_star2.check(mouse_pos) == True:
                                v = 0.5
                                star_list.append(Star(200, 300, 0, -v, 1000))
                                star_list.append(Star(400, 300, 0, v, 1000))
                                star_list.append(Star(600, 300, 0, -v, 1000))
                                star_list.append(Star(800, 300, 0, v, 1000))
                            if button_star3.check(mouse_pos) == True:
                                v = 0.5171
                                star_list.append(Star(200, 300, v, -v, 1000))
                                star_list.append(Star(400, 300, v, v, 1000))
                                star_list.append(Star(200, 500, -v, -v, 1000))
                                star_list.append(Star(400, 500, -v, v, 1000))

                            if event.button == 3:
                                p1 = event.pos[0], event.pos[1]
                                star_list.append(
                                    Star(event.pos[0], event.pos[1], 0, 0, 1000))
                        elif event.type == MOUSEBUTTONUP and event.button == 3:
                            p2 = event.pos[0], event.pos[1]
                            star_list[-1].set = set(p1, p2)
                            star_list[-1].v = Vec2d(p2[0] -
                                                    p1[0], p2[1]-p1[1])/100
                            p1, p2 = (0, 0), (0, 0)
                        elif event.type == KEYDOWN and event.key == K_SPACE:
                            initialize = not initialize
                        elif event.type == KEYDOWN and event.key == K_r:
                            star_list = []  # 星球列表
                            set_list = []
                    i=0
                    for star in star_list:
                        if not initialize:
                            star.update()
                        else:
                            
                            star.init(i)
                            i=i+1
                    if running1 == False:
                        screen.fill((255, 255, 255))
                    pygame.display.flip()
            elif button4.check(mouse_pos) == True:
                COLLTYPE_DEFAULT = 0
                COLLTYPE_MOUSE = 1
                demo = PhysicsDemo()
                demo.run()
            elif button5.check(mouse_pos) == True:

                running1 = True
                button5.surf.fill((255, 255, 255))
                screen.blit(button5.surf, (50, 275))
                ball_list = []
                line_list = []
                lines = []
                collide_event_list = []
                FPS = 60
                clock = pygame.time.Clock()
                font = pygame.font.SysFont("Arial", 16)
                white = (255, 255, 255)
                g = -0.1
                e = 0.8
                initialize = True
                max_path = 50
                draw_line1 = False
                draw_line2 = False
                p1, p2 = None,None
                line_list.append(Staic_Line((200, 400), (320, 400)))

                while running == True and running1 == True:
                    speed = 3
                    keys = pygame.key.get_pressed()
                    if(keys[K_LEFT]):
                        line_list[0].p1[0] -= speed
                        line_list[0].p2[0] -= speed
                    if (keys[K_RIGHT]):
                        line_list[0].p1[0] += speed
                        line_list[0].p2[0] += speed
                    if (keys[K_UP]):
                        line_list[0].p1[1] -= speed
                        line_list[0].p2[1] -= speed
                    if (keys[K_DOWN]):
                        line_list[0].p1[1] += speed
                        line_list[0].p2[1] += speed
                    line_list[0].b = line_list[0].p1[1]

                    mouse_pos = pygame.mouse.get_pos()
                    screen.fill((0, 0, 0))
                    font = pygame.font.Font(None, 16)
                    text = [
                        "Click the left mouse button to generate the ball",
                        "Click the mouse wheel to generate a dynamic bar",
                        "Click the right mouse button to generate a static bar ",
                        "press space to pause stimulation ",
                        "press R to reset "
                    ]
                    y = 5
                    for line in text:
                        text = font.render(line, 1, THECOLORS["white"])
                        screen.blit(text, (width - 300, y))
                        y += 10
                    screen.blit(button_exit.surf,
                                (width - dis_right - button_w, dis_h))
                    screen.blit(
                        back_size, (width - dis_right - button_w, dis_h))
                    back_size = pygame.transform.scale(
                        back, (button_w, button_h))
                    button_exit.surf = pygame.Surface((button_w, button_h))
                    if button_exit.check(mouse_pos) == True:
                        button_exit.surf.fill((255, 0, 0))
                    else:
                        button_exit.surf.fill((0, 0, 0))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            running = False
                        elif event.type == VIDEORESIZE:
                            width = event.size[0]
                            height = event.size[1]
                            button_w = int(width/8)
                            button_h = int(height/24)
                            dis_left = int(width/12)
                            dis_right = int(width/24)
                            dis_v = int(height/20)
                            dis_h = int(height/12)
                            dis_v2 = int(height/30)
                            screen = pygame.display.set_mode(
                                (width, height), pygame.RESIZABLE)
                        elif event.type == MOUSEBUTTONDOWN and button_exit.check(mouse_pos) == True:

                            running1 = False
                        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                            p1 = event.pos[0], event.pos[1]
                            ball_list.append(Ball(10, event.pos[0], event.pos[1], 0, 0))
                        elif event.type == MOUSEBUTTONUP and event.button == 1:
                            p2 = event.pos[0], event.pos[1]
                            if len(ball_list)>0:
                                ball_list[-1].set = set(p1, p2)
                                ball_list[-1].v = Vec2d(int(p2[0] - p1[0]),
                                                        int(p2[1] - p1[1])) / 10
                            p1, p2 = (0, 0), (0, 0)
                        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                            p3 = event.pos[0], event.pos[1]
                            draw_line1 = True
                        elif event.type == MOUSEBUTTONUP and event.button == 3:
                            p4 = event.pos[0], event.pos[1]
                            line_list.append(Staic_Line(p3, p4))
                            draw_line1 = False
                            p3, p4 = (0, 0), (0, 0)
                        elif event.type == MOUSEBUTTONDOWN and event.button == 2:
                            p5 = event.pos[0], event.pos[1]
                            draw_line2 = True
                        elif event.type == MOUSEBUTTONUP and event.button == 2:  # 定轴转动
                            p6 = event.pos[0], event.pos[1]
                            lines.append(Line(p5, p6, 0))
                            draw_line2 = False
                            p5, p6 = (0, 0), (0, 0)
                        elif event.type == KEYDOWN and event.key == K_SPACE:
                            initialize = not initialize
                        elif event.type == KEYDOWN and event.key == K_r:
                            ball_list = []
                            line_list = []
                            lines = []
                            collide_event_list = []
                            line_list.append(Staic_Line((200, 400), (320, 400)))

                        if draw_line1:
                            mouse_pos = pygame.mouse.get_pos()
                            pygame.draw.line(screen, white, p3, mouse_pos, 1)
                        if draw_line2:
                            mouse_pos = pygame.mouse.get_pos()
                            pygame.draw.line(screen, white, p5, mouse_pos, 1)
                    #for index in collide_event_list:
                    #    if index[0] == index[1]:
                    #        continue
                    #    if ball_list[index[0]].collision and ball_list[index[1]].collision:
                    #        ball_list[index[1]].v = -ball_list[index[1]].v
                    #        ball_list[index[0]].v = -ball_list[index[0]].v
                    #        continue
                    #    if ball_list[index[1]].collision:
                    #        ball_list[index[0]].v = -ball_list[index[0]].v
                    #        continue
                    #    if ball_list[index[0]].collision:
                    #        ball_list[index[1]].v = -ball_list[index[1]].v
                    #        continue
                    #    pos = ball_list[index[0]].pos - ball_list[index[1]].pos
                    #    pos = pos.normalized()
                    #    pos_vt = -Vec2d(pos[1], -pos[0])
                    #    v0 = ball_list[index[0]].v.dot(pos) * pos
                    #    v1 = ball_list[index[1]].v.dot(pos) * pos
                    #    if (v0 - v1).dot(pos) < 0:
                    #        v0_vt = ball_list[index[0]].v.dot(pos_vt) * pos_vt
                    #        v1_vt = ball_list[index[1]].v.dot(pos_vt) * pos_vt  # 垂直球心连线
                    #        k = ball_list[index[0]].m + ball_list[index[1]].m
                    #        k0 = ball_list[index[0]].m * v0 + ball_list[index[1]].m * v1
                    #        k1 = e * ball_list[index[1]].m * (v1 - v0)
                    #        k2 = e * ball_list[index[0]].m * (v0 - v1)
                    #        v0, v1 = (k0 + k1) / k, (k0 + k2) / k
#
#        ball_list[index[0]].v = v0 + v0_vt
#        ball_list[index[1]].v = v1 + v1_vt
#collide_event_list = []
                    for line in line_list:
                        line.draw()
                    update()






                    if running1 == False:
                        screen.fill((255, 255, 255))
                    pygame.display.flip()
                    time_passed = clock.tick(FPS)
            elif button6.check(mouse_pos) == True:
                running1 = True
                button6.surf.fill((255, 255, 255))
                screen.blit(button6.surf, (50, 275))
                ball_list = []
                line_list = []
                position = []
                initialize = True
                mid = width // 2
                top_point = mid, 0
                fps = 60
                g = 9.8
                p = 0, 0
                x, y = 0, 0
                SPACE = False


                draw_line = False
                p1 = 0, 0
                p2 = 0, 0

                while running == True and running1 == True:

                    mouse_pos = pygame.mouse.get_pos()
                    screen.fill((0, 0, 0))

                    screen.blit(button_exit.surf,
                                (width - dis_right - button_w, dis_h))
                    screen.blit(
                        back_size, (width - dis_right - button_w, dis_h))
                    back_size = pygame.transform.scale(
                        back, (button_w, button_h))
                    button_exit.surf = pygame.Surface((button_w, button_h))
                    if button_exit.check(mouse_pos) == True:
                        button_exit.surf.fill((255, 0, 0))
                    else:
                        button_exit.surf.fill((0, 0, 0))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            running = False
                        elif event.type == VIDEORESIZE:
                            width = event.size[0]
                            height = event.size[1]
                            mid = width // 2
                            button_w = int(width/8)
                            button_h = int(height/24)
                            dis_left = int(width/12)
                            dis_right = int(width/24)
                            dis_v = int(height/20)
                            dis_h = int(height/12)
                            dis_v2 = int(height/30)
                            screen = pygame.display.set_mode(
                                (width, height), pygame.RESIZABLE)
                        elif event.type == MOUSEBUTTONDOWN:
                            if button_exit.check(mouse_pos) == True:
                                running1 = False
                            if event.button == 1:
                                x0, y0 = pygame.mouse.get_pos()
                                theta0 = acos((Vec2d(x0, y0) - Vec2d(mid, 0)).dot(Vec2d(1, 0)) /
                                            (Vec2d(x0, y0) - Vec2d(mid, 0)).length) - pi * 0.5
                                x, y = x0, y0
                                #print x, y
                                while y > 0:
                                    ball_list.append(Ball2(10, x, y, 0, 0))
                                    line_list.append(Line2(x, y))
                                    y = y - 30 * cos(theta0)
                                    x = x + 30 * sin(theta0)
                                ball_list[-1].exist()
                                line_list[-1].exist()
                            if event.button == 3:
                                x, y = mouse_pos
                                #print x, y
                                ball_list.append(Ball2(10, x, y, 0, 0))
                                line_list.append(Line2(x, y))
                                ball_list[-1].exist()
                                line_list[-1].exist()
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            SPACE = not SPACE
                    if SPACE == False:
                        for ball in ball_list:
                            ball.exist()
                        for line in line_list:
                            line.exist()
                    if SPACE == True:
                        for ball in ball_list:
                            ball.update()
                        for line in line_list:
                            line.update()
                    if running1 == False:
                        screen.fill((255, 255, 255))
                    time_passed = clock.tick(fps)
                    pygame.display.flip()

    pygame.display.flip()
