from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout


def main_keyboard(q_connect, w_connect, e_connect,
                  r_connect, t_connect, y_connect,
                  u_connect, i_connect, o_connect,
                  p_connect, a_connect, s_connect,
                  d_connect, f_connect, g_connect,
                  h_connect, j_connect, k_connect,
                  l_connect, z_connect, x_connect,
                  c_connect, v_connect, b_connect,
                  n_connect, m_connect):

    layout_main_keyboard = QVBoxLayout()
    layout_main_keyboard.addLayout(line_1(q_connect, w_connect, e_connect, r_connect, t_connect,
                                          y_connect, u_connect, i_connect, o_connect, p_connect))
    layout_main_keyboard.addLayout(line_2(a_connect, s_connect, d_connect,
                                          f_connect, g_connect, h_connect,
                                          j_connect, k_connect, l_connect))
    layout_main_keyboard.addLayout(line_3(z_connect, x_connect, c_connect,
                                          v_connect, b_connect, n_connect,
                                          m_connect))

    return layout_main_keyboard


def line_1(q_connect, w_connect, e_connect, r_connect, t_connect,
           y_connect, u_connect, i_connect, o_connect, p_connect):

    q, w, e, r, t, y, u, i, o, p = QPushButton("Q"), QPushButton("W"), QPushButton("E"), QPushButton("R"),\
        QPushButton("T"), QPushButton("Y"), QPushButton("U"), QPushButton("I"), QPushButton("O"), QPushButton("P")

    q.clicked.connect(q_connect)
    w.clicked.connect(w_connect)
    e.clicked.connect(e_connect)
    r.clicked.connect(r_connect)
    t.clicked.connect(t_connect)
    y.clicked.connect(y_connect)
    u.clicked.connect(u_connect)
    i.clicked.connect(i_connect)
    o.clicked.connect(o_connect)
    p.clicked.connect(p_connect)

    layout_line_1 = QHBoxLayout()
    layout_line_1.addWidget(q)
    layout_line_1.addWidget(w)
    layout_line_1.addWidget(e)
    layout_line_1.addWidget(r)
    layout_line_1.addWidget(t)
    layout_line_1.addWidget(y)
    layout_line_1.addWidget(u)
    layout_line_1.addWidget(i)
    layout_line_1.addWidget(o)
    layout_line_1.addWidget(p)

    return layout_line_1


def line_2(a_connect, s_connect, d_connect,
           f_connect, g_connect, h_connect,
           j_connect, k_connect, l_connect):

    a, s, d, f, g, h, j, k, l = QPushButton("A"), QPushButton("S"), QPushButton("D"), QPushButton("F"),\
        QPushButton("G"), QPushButton("H"), QPushButton("J"), QPushButton("K"), QPushButton("L")

    a.clicked.connect(a_connect)
    s.clicked.connect(s_connect)
    d.clicked.connect(d_connect)
    f.clicked.connect(f_connect)
    g.clicked.connect(g_connect)
    h.clicked.connect(h_connect)
    j.clicked.connect(j_connect)
    k.clicked.connect(k_connect)
    l.clicked.connect(l_connect)

    layout_line_2 = QHBoxLayout()
    layout_line_2.addWidget(a)
    layout_line_2.addWidget(s)
    layout_line_2.addWidget(d)
    layout_line_2.addWidget(f)
    layout_line_2.addWidget(g)
    layout_line_2.addWidget(h)
    layout_line_2.addWidget(j)
    layout_line_2.addWidget(k)
    layout_line_2.addWidget(l)

    return layout_line_2


def line_3(z_connect, x_connect, c_connect,
           v_connect, b_connect, n_connect,
           m_connect):

    z, x, c, v, b, n, m = QPushButton("Z"), QPushButton("X"), QPushButton("C"), QPushButton("V"),\
        QPushButton("B"), QPushButton("N"), QPushButton("M")

    z.clicked.connect(z_connect)
    x.clicked.connect(x_connect)
    c.clicked.connect(c_connect)
    v.clicked.connect(v_connect)
    b.clicked.connect(b_connect)
    n.clicked.connect(n_connect)
    m.clicked.connect(m_connect)

    layout_line_3 = QHBoxLayout()
    layout_line_3.addWidget(z)
    layout_line_3.addWidget(x)
    layout_line_3.addWidget(c)
    layout_line_3.addWidget(v)
    layout_line_3.addWidget(b)
    layout_line_3.addWidget(n)
    layout_line_3.addWidget(m)

    return layout_line_3

