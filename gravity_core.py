import math

# Constantes físicas
G = 6.67430e-11        # Constante gravitacional (m³ kg⁻¹ s⁻²)
c = 299792458         # Velocidade da luz (m/s)


class BlackHole:
    def __init__(self, mass):
        """
        mass: massa do buraco negro (kg)
        """
        self.mass = mass

    def schwarzschild_radius(self):
        """
        Raio de Schwarzschild:
        rs = 2GM / c²
        """
        return (2 * G * self.mass) / (c ** 2)

    def gravitational_potential(self, r):
        """
        Potencial gravitacional clássico
        """
        return - (G * self.mass) / r

    def curvature(self, r):
        """
        Curvatura simplificada do espaço-tempo
        """
        return (2 * G * self.mass) / (c ** 2 * r)

    def is_inside_event_horizon(self, r):
        """
        Verifica se está dentro do horizonte de eventos
        """
        return r <= self.schwarzschild_radius()

    def time_dilation_factor(self, r):
        """
        Fator de dilatação temporal relativística:
        sqrt(1 - rs / r)
        """
        rs = self.schwarzschild_radius()

        if r <= rs:
            return 0.0  # tempo "congela" no horizonte (simulação)

        factor = math.sqrt(1 - (rs / r))

        # segurança numérica
        return max(factor, 0.001)