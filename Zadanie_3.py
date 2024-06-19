import numpy as np
import matplotlib.pyplot as plt


r0 = 100  # kapitał początkowy
lam = 0.5  # intensywność procesu Poissona
alpha = 2  # alpha w rozkładzie gamma
beta = 1    # beta w rozkładzie gamma
proloss = -1  # współczynnik zysku/straty
czas_max = 250  # maksymalny czas

surface = 0 # poziom, po przekroczeniu
            # którego odliczamy "upadek"

dive = 10   # czas, po upływie którego
            # firma bankrutuje
def p(t):
    return proloss * np.e**(-t)

time = 0            # początkowy czas jest równy 0
kapital = r0        # początkowy kapitał jest równy r0
capitals = [kapital] # lista kapitałów
times = [time]      # lista czasów


while time < czas_max:
    # krok czasu do następnego zdarzenia procesu Poissona
    skok = np.random.exponential(1 / lam)
    time += skok

    # aktualizujemy kapitał (zysk albo strata)
    kapital += proloss * skok

    # skok w procesie Poissona
    if np.random.rand() < lam * skok:
        damage = np.random.gamma(alpha, beta)
        kapital -= damage

    # zapisujemy wyniki
    times.append(time)
    capitals.append(kapital)

    # jeśli kapitał spadnie poniżej 0 i tam
    # się utrzyma przez 10 jednostek,
    # to STOP
    if kapital < 0:
        surface += skok
        if surface >= dive:
            break
    else:
        surface = 0
        
# tworzymy wykres
plt.figure(figsize=(12, 6))
plt.plot(times, capitals, label='Kapitał firmy')
plt.xlabel('Czas')
plt.ylabel('Kapitał')
plt.title('Kapitał firmy ubezpieczeniowej')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()