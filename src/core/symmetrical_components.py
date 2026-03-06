from cmath import rect, phase, polar
from math import radians, degrees

alpha = rect(1, radians(120))

def rect_to_polar(rect_form: complex):
    r, phi = polar(rect_form)
    return round(r, 2), round(degrees(phi), 2)


class SymmetricalComponents:

    @staticmethod
    def sequence_component(phase_a: tuple, phase_b: tuple, phase_c: tuple):
        # Convert tuples into complex numbers
        xa, xb, xc = (rect(r, radians(phi)) for r, phi in (phase_a, phase_b, phase_c))

        x0 = (xa + xb + xc) / 3
        x1 = (xa + alpha*xb + alpha**2*xc) / 3
        x2 = (xa + alpha**2*xb + alpha*xc) / 3

        return {
            'x0': rect_to_polar(x0),
            'x1': rect_to_polar(x1),
            'x2': rect_to_polar(x2),
        }
