# RealGEN

RealGEN es una aplicación web que permite generar imágenes **realistas** utilizando la API de Stable Diffusion Web UI. En lugar de escribir un prompt manualmente, se ofrecen controles interactivos (selectboxes, sliders, multiselect, etc.) para configurar los parámetros deseados. La aplicación construye automáticamente un prompt detallado en inglés, que se envía a la API para generar la imagen.

<div align="center">
  <img src="img/logo.png" alt="Logo RealGEN" width="400"/>
</div>

Este proyecto se realizó como parte del curso de *Máster de FP en Inteligencia Artificial y Big Data*.

---

## Integrantes del Equipo

| [![Jairo Andrades Bueno](https://github.com/jairopo.png?size=100)](https://github.com/jairopo) | [![Germán García Estévez](https://github.com/germangarest.png?size=100)](https://github.com/germangarest) |
|:---------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------:|
| **Jairo Andrades Bueno**                                                                      | **Germán García Estévez**                                                                      |

---

## Modelo Utilizado

- **Nombre:** Re3mix-realisticV2-Hyper
- **Descripción:**  
  Modelo completo en formato safetensors, diseñado para generar imágenes de alta fidelidad y realismo, capturando detalles precisos y una estética similar a la fotografía. Ideal para crear retratos, paisajes, escenas urbanas o naturales con gran nivel de detalle.
- **Enlace:** [Re3mix-realisticV2-Hyper en Civitai](https://civitai.com/models/560176/re3mix-realisticv2-hyper?modelVersionId=623806)

---

## Características de la Aplicación

- **Interfaz Web Interactiva:**  
  Desarrollada en *Streamlit*, RealGEN ofrece una experiencia intuitiva y moderna.
  
- **Selección de Parámetros:**  
  Permite personalizar distintos aspectos de la imagen:
  - **Tipo de Escena:**  
    Define el contexto visual. Opciones: *Retrato, Paisaje, Urbano, Natural, Nocturno*.
  - **Estado de Ánimo:**  
    Establece la atmósfera de la imagen. Opciones: *sereno, vibrante, melancólico, dinámico, misterioso*.
  - **Fondo o Ambientación:**  
    Selecciona el entorno. Opciones: *ciudad, naturaleza, interior, atardecer, amanecer*.
  - **Nivel de Detalle (%) y Nivel de Colorido (%):**  
    Dos sliders para ajustar el porcentaje de detalle y la saturación de colores.
  - **Elementos Adicionales:**  
    Permite añadir características extra mediante un menú multiselección: *efectos de luz, composición artística, iluminación dramática, alta resolución, detalles intrincados*.
    
- **Generación Automática del Prompt:**  
  Combina las opciones seleccionadas para construir un prompt en inglés, listo para ser enviado a la API.

- **Integración con la API de Stable Diffusion:**  
  Al pulsar el botón **"Generar Imagen"**, el prompt se envía a la API para generar la imagen, la cual se muestra en la interfaz. Además, se incluye la opción de descargar la imagen generada.

---

## Funcionamiento y Uso

1. **Configuración de Parámetros:**  
   - **Barra Lateral:**  
     Aquí se encuentran todos los controles interactivos:
     - **Selectboxes:** Para elegir el *Tipo de Escena*, *Estado de Ánimo* y *Fondo*.
     - **Sliders:** Para ajustar el *Nivel de Detalle* y el *Nivel de Colorido*.
     - **Multiselect:** Para seleccionar uno o varios *Elementos Adicionales*.
     
2. **Visualización del Prompt:**  
   La aplicación muestra, dentro de un contenedor expandible, el prompt generado a partir de las opciones seleccionadas.

3. **Generación y Descarga de la Imagen:**  
   - Al pulsar **"Generar Imagen"**, se envía el prompt a la API (mostrando un spinner durante el proceso).
   - La imagen generada se visualiza en la interfaz.
   - Se ofrece un botón para descargar la imagen en formato PNG.

---

## Capturas de Pantalla y Ejemplos

### Interfaz de la Aplicación

<div align="center">
<table>
  <tr>
    <td align="center"><img src="img/interfaz_1.png" alt="Interfaz Principal" width="300"/></td>
    <td align="center"><img src="img/interfaz_2.png" alt="Configuración de Parámetros" width="300"/></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><img src="img/interfaz_3.png" alt="Visualización del Prompt" width="300"/></td>
  </tr>
</table>
</div>

### Ejemplos de Imágenes Generadas

<div align="center">
<table>
  <tr>
    <td align="center"><img src="img/img_1.png" alt="Imagen 1" width="300"/></td>
    <td align="center"><img src="img/img_2.png" alt="Imagen 2" width="300"/></td>
  </tr>
  <tr>
    <td align="center"><img src="img/img_3.png" alt="Imagen 3" width="300"/></td>
    <td align="center"><img src="img/img_4.png" alt="Imagen 4" width="300"/></td>
  </tr>
</table>
</div>

### Parámetros Utilizados para Cada Imagen

<div align="center">
<table>
  <tr>
    <td align="center"><img src="img/parametros_1.png" alt="Parámetros Imagen 1" width="300"/></td>
    <td align="center"><img src="img/parametros_2.png" alt="Parámetros Imagen 2" width="300"/></td>
  </tr>
  <tr>
    <td align="center"><img src="img/parametros_3.png" alt="Parámetros Imagen 3" width="300"/></td>
    <td align="center"><img src="img/parametros_4.png" alt="Parámetros Imagen 4" width="300"/></td>
  </tr>
</table>
</div>

---

## Conclusiones

RealGEN demuestra cómo simplificar el proceso de generación de imágenes realistas mediante una interfaz intuitiva y controles personalizables. La integración con la API de Stable Diffusion y el uso del modelo **Re3mix-realisticV2-Hyper** permiten obtener resultados de alta calidad sin requerir conocimientos técnicos avanzados. Esta herramienta es ideal para exploraciones creativas y para generar contenido visual en diversos ámbitos.
