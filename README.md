# Asado Calculator

Este es mi **pet project**: una calculadora de asado para organizar asados fácilmente y sin quedarse corto ni gastar de más.  
¡Hecho con pasión por el asado y la programación!

---

## ¿Qué hace este proyecto?

Este proyecto te ayuda a calcular de manera precisa la cantidad de carne, chorizos, acompañamientos, pan, ensaladas, opciones vegetarianas y bebidas necesarias para un asado, según el tipo y cantidad de comensales.  
Incluye además explicaciones claras de cómo se hace cada cálculo para que puedas ajustar a tu gusto.

---

## Características principales

- **Cálculo por tipo de persona:** adultos (porción completa o moderada), niños, vegetarianos.
- **Detalle por tipo de corte de carne** (si seleccionás cortes específicos).
- **Acompañamientos:** mandioca, ensalada, pan.
- **Opciones vegetarianas** (si hay invitados vegetarianos).
- **Modo generoso:** incrementa las cantidades para que sobre.
- **Modo picada:** ajusta las cantidades para eventos tipo picada.
- **Cálculo de bebidas:** agua, gaseosa, cerveza y vino, con explicación de los promedios usados.
- **Explicación transparente:** cada resultado viene acompañado de una explicación de cómo se hizo el cálculo.

---

## ¿Cómo usarlo?

1. **Cloná el repo:**

   ```bash
   git clone https://github.com/tuusuario/asado-calculator.git
   cd asado-calculator
   ```

2. **Instalá las dependencias (si usás Python/Django):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Corré el servidor:**

   ```bash
   python manage.py runserver
   ```

4. **Abrí tu navegador en** [http://localhost:8000](http://localhost:8000)  
   Completá el formulario según tus invitados y preferencias.

---

## ¿Cómo se hacen los cálculos?

- **Carne:** 500g por adulto (porción completa), 350g por adulto (moderada), 250g por niño. Si seleccionás cortes, se reparte entre ellos.
- **Chorizos:** 1,5 por adulto (completa), 1 por adulto (moderada), 0,5 por niño.
- **Acompañamientos:** mandioca (250g/adulto, 150g/niño), ensalada (200g/adulto), pan (1 unidad/persona).
- **Vegetarianos:** 250g de opción vegetariana por persona.
- **Bebidas:** 0,5L de agua y 0,5L de gaseosa por persona; cada adulto suma 1L de cerveza y 0,5L de vino.
- **Modo generoso:** incrementa un 20% todas las cantidades.
- **Modo picada:** ajusta las cantidades para eventos tipo picada.

---

## ¿Cómo contribuyo?

1. Hacé un fork del repo.
2. Creá una rama para tu mejora o fix.
3. Hacé un PR con una breve descripción.

---

## Licencia

MIT

---

¡Que nunca falte el asado ni sobre el pan!