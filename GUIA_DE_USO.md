# Tebana Laboratorio Cervecero — Guia de Uso Completa

Bienvenido a tu sistema de gestion cervecera. Esta guia te explica **todo** lo que podes hacer, pantalla por pantalla, con ejemplos concretos. No necesitas saber de tecnologia: si sabes usar WhatsApp, sabes usar esto.

---

## Indice

1. [Como entrar a la app](#1-como-entrar-a-la-app)
2. [Instalarla como app en el iPhone](#2-instalarla-como-app-en-el-iphone)
3. [El Dashboard — pantalla principal](#3-el-dashboard--pantalla-principal)
4. [Recetas — crear, calcular y guardar](#4-recetas--crear-calcular-y-guardar)
5. [Inventario — control de ingredientes](#5-inventario--control-de-ingredientes)
6. [Lotes — seguimiento de produccion](#6-lotes--seguimiento-de-produccion)
7. [Ventas — pedidos de clientes](#7-ventas--pedidos-de-clientes)
8. [Clientes — datos de contacto](#8-clientes--datos-de-contacto)
9. [Barriles — control de kegs](#9-barriles--control-de-kegs)
10. [Flujo de trabajo completo paso a paso](#10-flujo-de-trabajo-completo-paso-a-paso)
11. [Como hacer un backup de tus datos](#11-como-hacer-un-backup-de-tus-datos)
12. [Preguntas frecuentes](#12-preguntas-frecuentes)
13. [Glosario cervecero](#13-glosario-cervecero)

---

## 1. Como entrar a la app

La app esta siempre disponible en internet, 24 horas al dia, los 7 dias de la semana. No necesitas tener la computadora prendida.

**Desde cualquier dispositivo (iPhone, PC, tablet):**

1. Abri el navegador (Safari en iPhone, Chrome o Edge en PC)
2. Escribi esta direccion exacta: **`etacar1nae.pythonanywhere.com`**
3. La pagina de inicio (Dashboard) carga automaticamente

> Si ves "Coming Soon" es porque falta configurar el servidor. Pedi ayuda para hacer el paso de "crear la web app" en PythonAnywhere (son 2 minutos y queda para siempre).

---

## 2. Instalarla como app en el iPhone

Para no tener que abrir Safari cada vez, podes instalarla como si fuera una app nativa, con icono propio y a pantalla completa.

**Paso a paso en iPhone:**

| Paso | Que haces | Que ves |
|---|---|---|
| 1 | Abri **Safari** (no Chrome, tiene que ser Safari) | La pagina del Dashboard |
| 2 | Toca el boton **Compartir** | Es el icono del cuadradito con una flecha hacia arriba. Esta en la barra de abajo (iPhone nuevo) o arriba (iPhone viejo) |
| 3 | Desliza el menu hacia abajo | Busca la opcion "Agregar a la pantalla de inicio" (tiene un icono de +) |
| 4 | Toca **"Agregar a la pantalla de inicio"** | Aparece una vista previa con el logo de Tebana |
| 5 | Esribi **"Tebana"** como nombre (o deja el que sale) | |
| 6 | Toca **Agregar** arriba a la derecha | Listo. Volves a la pantalla de inicio del iPhone |
| 7 | Busca el icono nuevo con el logo de Tebana | Tocalo. Se abre la app a pantalla completa, sin barra de Safari |

**Listo.** Ahora cada vez que toques el icono de Tebana entras directo a tu sistema de gestion.

> En **Android** es parecido: abri Chrome, toca los tres puntitos del menu, elegi "Agregar a la pantalla principal".

---

## 3. El Dashboard — pantalla principal

Es lo primero que ves al entrar. Te da un resumen instantaneo de como esta todo.

### Que muestra cada parte

**Fila de numeros grandes (tarjetas de estadisticas):**

| Numero | Significado |
|---|---|
| Recetas | Cuantas recetas de cerveza tenes guardadas |
| Lotes totales | Cuantas tandas de coccion registraste en total |
| Activos | Cuantas tandas estan en proceso ahora mismo (planificado, coccion, fermentando o madurando) |
| Listos | Cuantas tandas ya estan terminadas y listas para envasar/vender |
| Pedidos pend. | Cuantos pedidos de clientes estan pendientes de entregar o cobrar |

**Alertas (recuadros debajo de los numeros):**

- **Recuadro rojo**: "Stock bajo minimo". Aparece cuando algun ingrediente esta por debajo del minimo que configuraste. Muestra el nombre del ingrediente, cuanto te queda y cual es el minimo. Ejemplo: "Lupulo Cascade: 80 g / min 200 g". Esto significa que te quedan 80 gramos y deberias tener al menos 200. Toca el enlace "Ver todo" para ir al inventario.
- **Recuadro amarillo**: "Barriles prestados". Muestra cuantos kegs estan en casa de clientes y con quien. Muy util para no perder barriles.
- **Recuadro verde**: "Todo el stock sobre el minimo". Aparece cuando no hay nada critico. Buena señal.

**Lotes recientes (tabla de abajo):**

Muestra los ultimos 5 lotes que creaste. De cada uno ves:
- **Nombre**: ej. "IPA Lote #3". Tocalo para ver el detalle completo y la grafica de fermentacion.
- **Receta**: de que receta salio. Si no tiene receta asociada, dice "-".
- **Estado**: una etiqueta de color. Cada color significa una etapa del proceso:
  - Amarillo: planificado o en coccion
  - Azul: fermentando
  - Verde: listo o envasado
  - Gris: vendido
- **Fecha**: cuando empezo este lote

**Botones rapidos (fila inferior):**

Cuatro botones de colores para crear cosas nuevas con un solo toque:
- **+ Nueva Receta** (ambar): crear una receta desde cero
- **+ Nuevo Lote** (gris): iniciar una tanda de produccion
- **+ Nueva Venta** (gris): registrar un pedido de un cliente
- **+ Ingrediente** (gris): agregar algo al inventario

---

## 4. Recetas — crear, calcular y guardar

El corazon cervecero de la app. Aca diseñas tus recetas y la app calcula automaticamente IBU, ABV, color y atenuacion.

### Pantalla: Lista de recetas

Tabla con todas tus recetas. Muestra nombre, estilo, OG, IBU y ABV estimado.

- Toca el **nombre** de cualquier receta para verla en detalle.
- Toca **+ Nueva** arriba a la derecha para crear una.

### Pantalla: Nueva Receta (el formulario mas importante)

Esta pantalla tiene 3 secciones principales.

#### Seccion 1: Datos generales

| Campo | Que poner | Ejemplo |
|---|---|---|
| **Nombre** | Como le llamas a esta cerveza | "Golden Ale Tebana" |
| **Estilo** | El estilo BJCP | "American IPA", "Kolsch", "Stout" |
| **Vol. objetivo (L)** | Cuantos litros vas a producir en esta receta | `20` (si haces tandas de 20 litros) o `40` |
| **Eficiencia (%)** | Que tan eficiente es tu macerado. Normalmente entre 65 y 75%. Si no sabes, deja `70` | `70` |
| **OG objetivo** | Densidad inicial que esperas. Se mide con el densimetro antes de fermentar. | `1.050` (una cerveza de fuerza media) |
| **FG objetivo** | Densidad final esperada. Se mide cuando termina de fermentar. | `1.012` |
| **Notas** | Cualquier cosa que quieras recordar sobre esta receta | "Primer intento, ajustar lupulo de aroma" |

> **No necesitas calcular nada a mano.** La app hace todos los calculos automaticamente con los ingredientes que agregues.

#### Seccion 2: Ingredientes (la parte clave)

Aca elegis que lleva tu cerveza. Toca el boton **+ Agregar ingrediente** para cada cosa que lleve la receta.

Cada fila de ingrediente tiene:

1. **Tipo**: elegi entre:
   - **Malta**: granos que aportan azucares fermentables y color. Ej: "Pilsner", "Munich", "Caramel 60L"
   - **Lupulo**: aporta amargor, sabor y aroma. Ej: "Cascade", "Citra", "Saaz"
   - **Levadura**: el microorganismo que fermenta. Ej: "US-05", "S-04"
   - **Adjunto**: cualquier cosa extra. Ej: avena, trigo, miel, cascara de naranja

2. **Ingrediente**: elegi del menu desplegable. **Este menu muestra lo que tenes cargado en el Inventario.** Por eso conviene cargar primero los ingredientes en Inventario (seccion 5 de esta guia).

3. **Cantidad y Unidad**: cuanto lleva. En kg, g, lb, oz, o litros.

4. **Campos extra para lupulos** (solo aparecen si elegis tipo "lupulo"):
   - **Tiempo (min)**: cuantos minutos hierve este lupulo. `60` = principio del hervor (amargor), `15` = mitad (sabor), `5` = final (aroma), `0` = dry hop (en frio, despues de hervir)
   - **Uso**: amargor / sabor / aroma / dry hop. Esto es mas para que vos organices las adiciones. El calculo de IBU usa el tiempo y el % alfa.

#### Seccion 3: Calculos estimados (se actualizan solos)

A medida que agregas ingredientes, los 4 recuadros de abajo se actualizan instantaneamente:

| Calculo | Que significa | Valores tipicos |
|---|---|---|
| **ABV** | Alcohol por volumen. Que tan fuerte es la cerveza. | 4-5% session, 5-7% normal, 7-10% fuerte |
| **IBU** | Unidades de amargor. Que tan amarga es. | 10-20 suave, 20-40 media, 40-60 amarga, 60+ muy amarga |
| **Color SRM** | Que tan oscura. | 2-5 dorada, 5-15 ambar, 15-25 marron, 25+ negra |
| **Atenuacion** | % de azucares que la levadura va a consumir. | 70-80% tipico para ales |

> **Tip:** juga con las cantidades y mira como cambian los numeros en vivo. Es la mejor forma de diseñar una receta balanceada.

**Cuando termines**, toca el boton **Guardar Receta** (ambar, abajo).

### Pantalla: Ver Receta

Muestra todo el detalle de la receta ya guardada.

- **Tarjetas superiores**: volumen, OG/FG, ABV, IBU, color y eficiencia, todo calculado.
- **Estilo**: si lo pusiste, aparece aca.
- **Tabla de ingredientes**:
  - Nombre del ingrediente
  - Tipo con etiqueta de color
  - Cantidad exacta y unidad. Si es lupulo, muestra tambien el tiempo y uso
  - **% Grilla**: que porcentaje de la receta es esa malta (solo maltas). Ej: si tu receta lleva 4 kg de Pilsner y 1 kg de Munich, Pilsner es 80% y Munich 20%.
  - **IBU**: cuanto amargor aporta cada lupulo individualmente
  - **SRM**: cuanto color aporta cada malta individualmente
- **Notas**: lo que escribiste en el campo de notas.
- **Botones**: Editar (para modificar) y Eliminar (cuidado, no se puede deshacer).

### Pantalla: Editar Receta

Igual que crear, pero con todos los datos precargados. Podes cambiar lo que quieras y guardar.

---

## 5. Inventario — control de ingredientes

Aca manejas el stock de todo lo que usas para hacer cerveza: maltas, lupulos, levaduras y otros insumos.

### Pantalla: Lista de inventario

**Filtros (pildoras de colores arriba):**

| Filtro | Que muestra |
|---|---|
| Todos | Todo el inventario |
| Malta | Solo maltas |
| Lupulo | Solo lupulos |
| Levadura | Solo levaduras |
| Adjunto | Solo adjuntos |
| Stock bajo (roja) | Solo ingredientes que estan en o debajo del minimo |

**Tabla de ingredientes:**

| Columna | Que muestra |
|---|---|
| Nombre | Click para editar ese ingrediente. Si esta en rojo, esta bajo el minimo |
| Tipo | Etiqueta de color con la categoria |
| Stock | Cantidad actual + botones +/- para ajuste rapido. Si esta bajo el minimo, el numero aparece en amarillo |
| Precio | Cuanto pagaste por ese ingrediente |

**Ajuste rapido de stock (los botones + y -):**

Cada ingrediente tiene dos mini-formularios inline:
- **Boton +**: pones un numero y tocas +. Suma esa cantidad al stock.
- **Boton -**: pones un numero y tocas -. Resta esa cantidad al stock (nunca baja de 0).

> Esto es util para ajustar stock al vuelo sin entrar a editar todo el ingrediente. Ej: gastaste 500 g de una malta en una coccion, pones 0.5 en el - y listo.

**Alertas visuales:**

- **Fondo amarillo** en la fila: ese ingrediente esta bajo el minimo.
- **Nombre en amarillo**: igual, stock critico.
- **Icono de reloj** junto al nombre: la fecha de caducidad ya paso.

### Pantalla: Nuevo Ingrediente

**Campos basicos (todos los tipos):**

| Campo | Que poner | Ejemplo |
|---|---|---|
| Nombre | Como se llama | "Malta Pilsner", "Lupulo Cascade", "Levadura US-05" |
| Tipo | Categoria | malta / lupulo / levadura / adjunto |
| Cantidad inicial | Cuanto tenes al empezar | `5` |
| Unidad | En que medis | kg para granos, g para lupulos, unidad para levaduras |
| Stock minimo | Con cuanto queres que te avise | `2` (cuando bajes de 2 kg, alerta) |
| Precio | Cuanto pagaste por esta cantidad | `2500` (pesos) |
| Lote / Proveedor | Para trazabilidad | "Lote #456 - Proveedor X" |
| Caducidad | Fecha de vencimiento | Usa el selector de fecha |

**Campos especiales (aparecen segun el tipo):**

| Tipo seleccionado | Campo extra | Para que sirve |
|---|---|---|
| **Lupulo** | % Alfa acido | El porcentaje de alfa-acidos del lupulo. **Critico para calcular IBU en las recetas.** Viene en el paquete del lupulo. Ej: Cascade 5.5% |
| **Malta** | Lovibond (color) | El color de la malta en grados Lovibond. **Critico para calcular SRM en las recetas.** Viene en la ficha tecnica. Ej: Pilsner 1.5L, Munich 10L, Chocolate 350L |

> **Importante**: si no cargas el % alfa en los lupulos y el Lovibond en las maltas, las calculadoras de recetas no van a poder calcular IBU ni color. Carga siempre estos datos.

### Pantalla: Editar Ingrediente

Igual que Nuevo, con los datos precargados. Botones: Guardar, Cancelar, Eliminar.

---

## 6. Lotes — seguimiento de produccion

Cada vez que cocinas una tanda de cerveza, creas un "lote". El lote sigue todo el proceso de vida de esa cerveza.

### Pantalla: Lista de lotes

**Filtros por estado** (pildoras arriba):

Los 7 estados del proceso cervecero:
1. **Planificado**: lo creaste pero todavia no empezaste a cocinar
2. **Coccion**: estas en el dia de coccion (macerando, hirviendo, enfriando)
3. **Fermentando**: ya inocularon levadura y esta en el fermentador
4. **Madurando**: fermentacion principal terminada, madurando en frio
5. **Listo**: la cerveza esta terminada, lista para envasar
6. **Envasado**: ya esta en botellas, latas o barriles
7. **Vendido**: se vendio todo

### Pantalla: Nuevo Lote

| Campo | Que poner |
|---|---|
| Nombre del lote | Un identificador unico. Ej: "IPA #4", "Golden Ale - 15/07" |
| Receta base | Elegi del menu la receta que vas a usar. Si no tenes una, dejalo vacio |
| Volumen objetivo (L) | Cuantos litros planeas producir en esta tanda |
| Notas | Cualquier cosa particular de este lote. Ej: "Use agua de osmosis", "La malta Munich estaba un poco vieja" |

**Al guardar**, si vinculaste una receta, el sistema **descuenta automaticamente** del inventario los ingredientes que usa la receta. No tenes que hacerlo a mano.

### Pantalla: Ver Lote (la mas util del sistema)

**Seccion superior — Tarjetas:**

- **Estado**: un menu desplegable para cambiar el estado del lote. Selecciona el nuevo estado y toca "Actualizar". Ej: pasa de "fermentando" a "madurando" cuando corresponda.
- **Receta**: que receta base usaste. Tocala para ver la receta.
- **Volumen**: litros objetivo de la tanda.
- **Inicio**: fecha en que arranco este lote.
- **OG real**: la densidad inicial medida con tu densimetro el dia de coccion.
- **FG real**: la densidad final medida cuando termino de fermentar.

**Seccion central — Registro de fermentacion:**

Esta es la parte mas importante para el control de calidad.

- **Boton "+ Registrar"**: lo tocas para anotar una medicion. Se abre un formulario chiquito con:
  - **Temperatura (C)**: la temperatura del fermentador en ese momento. Ej: `19.5`
  - **Gravedad**: la densidad medida con el densimetro o refractometro. Ej: `1.045`
  - **Notas**: algo que quieras registrar. Ej: "Burbujeo activo", "Krausen alto"
  - Toca **"Guardar registro"** y se agrega a la tabla y la grafica.

- **Grafico**: muestra dos curvas superpuestas:
  - Linea ambar (Gravedad): como baja la densidad a lo largo de los dias. Deberia bajar rapido los primeros dias y despues estabilizarse.
  - Linea naranja (Temperatura): la temperatura de fermentacion dia a dia.

- **Tabla de registros**: el historial completo de todas las mediciones, ordenadas por fecha.

> **Consejo**: registra la gravedad y temperatura todos los dias o dia por medio durante la fermentacion activa (primeros 5-7 dias). Despues cada 2-3 dias. Asi tenes una curva completa y podes detectar problemas a tiempo (ej: fermentacion estancada).

---

## 7. Ventas — pedidos de clientes

Registra aca cada venta que haces, ya sea a un bar, restaurante o venta directa.

### Pantalla: Lista de pedidos

Tabla con todos los pedidos historicos. Muestra:
- **Cliente**: a quien le vendiste. Tocalo para ver el detalle del pedido.
- **Fecha**: cuando se hizo el pedido.
- **Estado**: pendiente, entregado, pagado o cancelado. Cada uno con su color.
- **Total**: monto total del pedido.

### Pantalla: Nuevo Pedido

1. **Cliente**: elegi del menu. Si no aparece nadie, anda a la seccion Clientes y crea uno primero.
2. **Productos**: toca **+ Agregar producto** por cada cosa que vendes en este pedido:
   - **Producto**: nombre de la cerveza. Ej: "Golden Ale", "IPA", "Kolsch"
   - **Cantidad**: cuantas unidades. Si vendes barriles de 20L, pone `1` (o `2` si son dos barriles). Si vendes botellas, pone la cantidad.
   - **Precio ($)**: precio por unidad
3. **Notas**: cualquier detalle. Ej: "Entregar el viernes", "Dejo 2 kegs vacios"
4. Toca **Crear Pedido**

### Pantalla: Ver Pedido

- **Datos del cliente** y fecha del pedido.
- **Cambiar estado**: menu desplegable para mover el pedido por su ciclo: Pendiente → Entregado → Pagado. (Tambien podes marcar como Cancelado si no se concreto.)
- **Tabla de productos**: detalle de cada linea con cantidad, precio unitario y subtotal.
- **Total** en grande al pie de la tabla.
- **Notas** del pedido.
- **Boton Eliminar**: borra el pedido completo (cuidado).

---

## 8. Clientes — datos de contacto

Aca guardas la informacion de bares, restaurantes, negocios y particulares a los que les vendes.

### Pantalla: Lista de clientes

Tabla con nombre, contacto y tipo de cada cliente. Toca el nombre para editar.

### Pantalla: Nuevo Cliente

| Campo | Que poner | Ejemplo |
|---|---|---|
| Nombre | Nombre del bar, restaurante o persona | "Bar El Growler", "Restaurant La Esquina" |
| Contacto | Telefono, email o como comunicarte | "Juan - 11 1234 5678" |
| Tipo | Categoria | bar / restaurante / retail / particular / otro |
| Direccion | Donde queda | "Av. Siempre Viva 742" |
| Notas | Info adicional | "Prefiere IPA, pide cada 2 semanas" |

---

## 9. Barriles — control de kegs

Como tenes 14 barriles, este modulo te ayuda a no perder ninguno.

### Pantalla: Lista de barriles

Cada barril muestra:

| Columna | Que muestra |
|---|---|
| Nombre | ID del barril (ej: "Keg #1", "Barril 20L azul") |
| Capacidad | Cuantos litros entran |
| Contenido | Que cerveza tiene adentro ahora. Ej: "Golden Ale" |
| Estado | Donde esta el barril |

**Si el barril esta en casa:**
- Muestra "En casa" o la ubicacion que le pusiste (ej: "Camara fria").
- Tenes un menu desplegable con los clientes y un boton **Prestar**: elegis el cliente y tocas Prestar. El barril queda marcado con fondo amarillo.

**Si el barril esta prestado:**
- Muestra el nombre del cliente y la fecha en que se lo llevo.
- Tiene un boton **Devolver**: cuando el barril vuelve, lo tocas y el barril vuelve a "En casa".

> En el Dashboard principal ves cuantos barriles tenes prestados y a quien, asi de un vistazo sabes que kegs tenes que recuperar.

---

## 10. Flujo de trabajo completo paso a paso

Esta es la secuencia ideal de uso, desde que compras ingredientes hasta que vendes la cerveza.

### Paso 1: Cargar ingredientes en Inventario

Anda a **Inventario** → **+ Ingrediente**. Carga todo lo que tenes:

```
Ejemplo:
- Malta Pilsner, 25 kg, Lovibond 1.5, stock minimo 10 kg
- Malta Munich, 5 kg, Lovibond 10, stock minimo 2 kg  
- Lupulo Cascade, 200 g, Alfa acido 5.5%, stock minimo 50 g
- Lupulo Citra, 150 g, Alfa acido 12%, stock minimo 50 g
- Levadura US-05, 3 unidades, stock minimo 1
```

**Tiempo estimado:** 5 minutos la primera vez. Despues solo mantenimiento.

### Paso 2: Crear una receta

Anda a **Recetas** → **+ Nueva Receta**.

```
Ejemplo de Golden Ale:
- Nombre: "Golden Ale Tebana"
- Estilo: "Blonde Ale"
- Volumen: 20 L
- Eficiencia: 70%
- OG: 1.048, FG: 1.010

Ingredientes:
- Malta Pilsner: 4 kg
- Malta Munich: 0.5 kg
- Lupulo Cascade: 20 g, 60 min, amargor
- Lupulo Cascade: 15 g, 10 min, aroma
- Levadura US-05: 1 unidad
```

Mientras agregas ingredientes, mira los calculos abajo. La app te dice ABV, IBU, color y atenuacion en tiempo real.

**Tiempo estimado:** 2 minutos por receta.

### Paso 3: Crear un lote cuando cocinas

Anda a **Lotes** → **+ Nuevo Lote**.

```
Ejemplo:
- Nombre: "Golden Ale - Lote #3"  
- Receta base: "Golden Ale Tebana"
- Volumen: 20 L
```

Al guardar, el stock se descuenta solo. La Malta Pilsner pasa de 25 kg a 21 kg, etc.

**Tiempo estimado:** 30 segundos.

### Paso 4: Registrar la fermentacion

Anda al lote que creaste (tocalo en la lista de Lotes).

**Dia de coccion:** toca "+ Registrar". Pone la temperatura inicial y la gravedad OG real que mediste con el densimetro. Ej: temperatura 20, gravedad 1.048.
Toca "Guardar registro".

**Cada dia despues:** toca "+ Registrar" y anota la temperatura y la gravedad actual. La grafica se va armando sola.

**Cuando la gravedad se estabiliza** (mismo valor 3 dias seguidos): la fermentacion termino. Anda al menu de estado y cambialo a "madurando" o "listo".

**Tiempo estimado:** 20 segundos por dia.

### Paso 5: Crear clientes

Anda a **Clientes** → **+ Nuevo**. Carga los bares y restaurantes a los que les vendes.

**Tiempo estimado:** 1 minuto por cliente (solo la primera vez).

### Paso 6: Registrar ventas

Anda a **Ventas** → **+ Nuevo Pedido**. Cada vez que entregas cerveza, crea un pedido:

```
Ejemplo:
- Cliente: "Bar El Growler"
- Producto: Golden Ale, Cantidad: 1, Precio: $15000
- Producto: IPA, Cantidad: 2, Precio: $16000
- Notas: "Lleva 1 keg de Golden y 2 de IPA. Traer kegs vacios de la entrega anterior"
```

Cuando entregas, cambia el estado a "Entregado". Cuando cobras, cambialo a "Pagado".

**Tiempo estimado:** 1 minuto por pedido.

### Paso 7: Controlar barriles

Anda a **Barriles**. Cuando entregas cerveza a un cliente, prestale el barril: elegi el cliente del menu y toca "Prestar". El barril queda en amarillo.

Cuando te devuelven el barril vacio, toca "Devolver". Vuelve a "En casa".

---

## 11. Como hacer un backup de tus datos

Tus recetas, inventario, lotes y ventas estan guardados en un solo archivo en el servidor. Conviene hacer una copia de seguridad cada tanto.

1. En pythonanywhere.com, abri una **consola Bash** (pestaña Consoles)
2. Escribi y presiona Enter:

```bash
cp ~/InventarioTebana/data/cerveceria.db ~/backup_$(date +%Y%m%d).db
```

3. Listo. Se creo un archivo `backup_20260714.db` (con la fecha de hoy) en tu carpeta principal.

**Para restaurar** desde un backup (si pasa algo):
```bash
cp ~/backup_20260714.db ~/InventarioTebana/data/cerveceria.db
```

**Cada cuanto?** Una vez por semana o cada 15 dias es suficiente. Tambien hace backup antes de hacer muchos cambios de una vez.

---

## 12. Preguntas frecuentes

### "La app no carga, dice Coming Soon"
Falta crear la web app en PythonAnywhere. Anda a la pestaña Web → Add a new web app → Manual config → Python 3.10. Despues segui los pasos de configuracion. Si necesitas ayuda, pedila.

### "No me aparecen ingredientes para elegir en las recetas"
Primero tenes que cargar los ingredientes en **Inventario**. El menu de recetas solo muestra lo que existe en el inventario.

### "Los calculos de IBU y color no funcionan"
Para que la app calcule IBU, los **lupulos** necesitan tener cargado el **% de alfa-acido** en el inventario. Para que calcule color (SRM), las **maltas** necesitan tener cargado el **Lovibond**. Edita esos ingredientes y completa esos campos.

### "Como calculo la eficiencia de mi equipo?"
La eficiencia la pones vos en base a tu experiencia. Si no sabes, empeza con 70%. Si tu OG real siempre sale mas alto que el objetivo, tu eficiencia es mayor (subila a 75%). Si sale mas bajo, tu eficiencia es menor (bajala a 65%). Con el tiempo le agarras la mano.

### "Se puede usar sin internet?"
En el iPhone, si la instalaste como PWA y ya la abriste al menos una vez con internet, algunas pantallas quedan en cache y podes navegar sin conexion. Pero para guardar datos nuevos necesitas internet (los datos se guardan en el servidor).

### "Se me borraron los datos"
No deberia pasar porque la base de datos es persistente en PythonAnywhere. Si paso algo raro, restaura desde tu backup (seccion 11). Por eso es importante hacer backups.

### "Puedo agregar mas de un usuario?"
Por ahora es monousuario. Si en el futuro necesitas que varias personas usen la app con distintos permisos (ej: el maestro cervecero vs el que hace ventas), se puede agregar.

### "Se pueden exportar recetas a BeerXML?"
No todavia, pero esta planeado. BeerXML es el formato estandar que usan programas como BrewersFriend y Brewfather. Cuando este listo, vas a poder compartir recetas entre plataformas.

---

## 13. Glosario cervecero

| Termino | Significado |
|---|---|
| **OG** (Original Gravity) | Densidad del mosto antes de fermentar. Se mide con densimetro. Ej: 1.050 |
| **FG** (Final Gravity) | Densidad despues de fermentar. Ej: 1.012 |
| **ABV** (Alcohol By Volume) | Porcentaje de alcohol. Se calcula: (OG - FG) x 131.25 |
| **IBU** (International Bitterness Units) | Unidad de amargor. Aportado por los lupulos durante el hervor |
| **SRM** (Standard Reference Method) | Escala de color de la cerveza. 2 = muy clara, 40+ = negra |
| **Eficiencia** | Que porcentaje de los azucares del grano lograste extraer en el macerado |
| **Atenuacion** | Que porcentaje de azucares fermento la levadura |
| **Lovibond (L)** | Unidad de color de las maltas. Pilsner ~1.5L, Munich ~10L, Chocolate ~350L |
| **Alfa-acidos** | Compuestos del lupulo que aportan amargor. Viene en % en el paquete |
| **Macerado / Mash** | Proceso de remojar los granos molidos en agua caliente para extraer azucares |
| **Hervor / Boil** | Coccion del mosto con lupulos (normalmente 60-90 minutos) |
| **Dry Hop** | Agregar lupulo en frio, despues de la fermentacion, solo para aroma |
| **Krausen** | Espuma densa que se forma arriba del mosto durante la fermentacion activa |
| **Trub** | Sedimento de proteinas y lupulo que queda en el fondo despues del hervor |
