import colorsys
import math
import turtle

# Configuração da tela (500x500, fundo escuro #080818)
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.bgcolor("#080818")
screen.title("Arco-Íris de Espiral")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()


def hsl_to_hex(h_deg, s_pct, l_pct):
    # Converte HSL (graus 0-360, % 0-100, % 0-100) para hex (#RRGGBB)
    r, g, b = colorsys.hls_to_rgb((h_deg % 360) / 360.0, l_pct / 100.0, s_pct / 100.0)
    return f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"


# Desenha os 180 círculos em espiral (no turtle, (0, 0) já é o centro)
for i in range(180):
    a = i * 0.18
    r = 5 + i * 1.15
    x = r * math.cos(a)
    y = r * math.sin(a)
    radius = 3 + i % 5

    cor = hsl_to_hex(i * 4 % 360, 100, 60)
    t.goto(x, y - radius)
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Círculo branco central (raio 9)
center_radius = 9
t.goto(0, -center_radius)
t.fillcolor("white")
t.begin_fill()
t.circle(center_radius)
t.end_fill()

screen.update()
screen.mainloop()