# RealGEN

RealGEN es una aplicación web que permite generar imágenes **realistas** utilizando la API de Stable Diffusion Web UI. En lugar de que el usuario tenga que escribir un prompt manualmente, se ofrecen diversos controles interactivos (selectboxes, sliders, multiselect, etc.) para configurar los parámetros deseados. La aplicación traduce estas selecciones en un prompt detallado en inglés que se envía a la API para generar la imagen.

<img src="img/logo.png" alt="Logo RealGEN" width="400"/>

Este proyecto se realizó como parte del curso de *Máster de FP en Inteligencia Artificial y Big Data*.

## Integrantes del equipo

| [![Jairo Andrades Bueno](https://github.com/jairopo.png?size=100)](https://github.com/jairopo) | [![Germán García Estévez](https://github.com/germangarest.png?size=100)](https://github.com/germangarest) |
|:----------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------:|
| **Jairo Andrades Bueno**                                                                       | **Germán García Estévez**                                                                       |

## Modelo Utilizado

- **Nombre:** Re3mix-realisticV2-Hyper
- **Descripción:**  
  Este modelo completo en formato safetensors está diseñado para generar imágenes de alta fidelidad y realismo, capturando detalles precisos y una estética visual similar a la fotografía. Es ideal para crear retratos, paisajes, escenas urbanas o naturales con un nivel de detalle excepcional.
- **Enlace:** [Re3mix-realisticV2-Hyper en Civitai](https://civitai.com/models/560176/re3mix-realisticv2-hyper?modelVersionId=623806)

## Características de la Aplicación

- **Interfaz Web Interactiva:**  
  Desarrollada en *Streamlit*, RealGEN ofrece una experiencia intuitiva y visualmente atractiva.
  
- **Selección de Parámetros:**  
  La aplicación permite personalizar diversos aspectos de la imagen a generar:
  - **Tipo de Escena:**  
    Define el contexto visual de la imagen. Las opciones disponibles son:
    - *Retrato*
    - *Paisaje*
    - *Urbano*
    - *Natural*
    - *Nocturno*
    
  - **Estado de Ánimo:**  
    Determina la atmósfera o sensación que transmitirá la imagen. Las opciones son:
    - *sereno*
    - *vibrante*
    - *melancólico*
    - *dinámico*
    - *misterioso*
    
  - **Fondo o Ambientación:**  
    Selecciona el entorno en el que se situará la imagen. Las opciones incluyen:
    - *ciudad*
    - *naturaleza*
    - *interior*
    - *atardecer*
    - *amanecer*
    
  - **Nivel de Detalle (%) y Nivel de Colorido (%):**  
    Dos controles deslizantes (sliders) permiten ajustar el porcentaje de detalle y la saturación de los colores, respectivamente.
    
  - **Elementos Adicionales:**  
    A través de un menú multiselección, se pueden añadir características extra que enriquecen la imagen, tales como:
    - *efectos de luz*
    - *composición artística*
    - *iluminación dramática*
    - *alta resolución*
    - *detalles intrincados*

- **Generación Automática del Prompt:**  
  Con base en las opciones seleccionadas, la aplicación construye un prompt en inglés que describe de forma detallada la imagen que se desea generar. Esto facilita la interacción con la API de Stable Diffusion.

- **Integración con la API de Stable Diffusion:**  
  Al presionar el botón **"Generar Imagen"**, el prompt y los parámetros configurados se envían a la API, la cual genera la imagen correspondiente. Además, se muestra un spinner durante la generación y se ofrece la opción de descargar la imagen resultante.

## Funcionamiento y Uso de la Aplicación

1. **Configuración de Parámetros:**  
   - **Barra Lateral:**  
     Aquí se ubican todos los controles interactivos:
     - **Selectboxes:** Para elegir el *Tipo de Escena*, *Estado de Ánimo* y *Fondo*.
     - **Sliders:** Para ajustar el *Nivel de Detalle* y el *Nivel de Colorido*.
     - **Multiselect:** Para seleccionar uno o varios *Elementos Adicionales*.
     
2. **Visualización del Prompt Generado:**  
   Una vez establecidos los parámetros, la aplicación muestra el prompt generado dentro de una sección expandible. Esto permite revisar la descripción exacta que se enviará a la API.

3. **Generación y Visualización de la Imagen:**  
   - Al pulsar el botón **"Generar Imagen"**, se envían los datos a la API.
   - Durante la generación, se muestra un spinner para indicar que el proceso está en curso.
   - La imagen generada se muestra en la interfaz y, además, se ofrece un botón para descargarla en formato PNG.

## Capturas de Pantalla y Ejemplos

A continuación se presentan algunas capturas de pantalla que muestran el funcionamiento de la aplicación, junto con ejemplos de imágenes generadas y los parámetros utilizados para cada una.

### Capturas de la Interfaz

- **Interfaz Principal:**  
  <img src="interfaz_1.png" alt="Interfaz Principal" width="400"/>
  
- **Menú Lateral y Configuración de Parámetros:**  
  <img src="interfaz_2.png" alt="Configuración de Parámetros" width="400"/>
  
- **Visualización del Prompt Generado:**  
  <img src="interfaz_3.png" alt="Visualización del Prompt" width="400"/>

### Ejemplos de Imágenes Generadas

- **Imagen 1:**  
  <img src="img_1.png" alt="Imagen 1" width="400"/>
  - **Parámetros Utilizados:**  
    <img src="parametros_1.png" alt="Parámetros Imagen 1" width="400"/>
    
- **Imagen 2:**  
  <img src="img_2.png" alt="Imagen 2" width="400"/>
  - **Parámetros Utilizados:**  
    <img src="parametros_2.png" alt="Parámetros Imagen 2" width="400"/>
    
- **Imagen 3:**  
  <img src="img_3.png" alt="Imagen 3" width="400"/>
  - **Parámetros Utilizados:**  
    <img src="parametros_3.png" alt="Parámetros Imagen 3" width="400"/>
    
- **Imagen 4:**  
  <img src="img_4.png" alt="Imagen 4" width="400"/>
  - **Parámetros Utilizados:**  
    <img src="parametros_4.png" alt="Parámetros Imagen 4" width="400"/>

## Conclusiones

RealGEN demuestra cómo se puede simplificar el proceso de generación de imágenes realistas mediante una interfaz intuitiva y controles personalizables. Gracias a la integración con la API de Stable Diffusion y al uso del modelo **Re3mix-realisticV2-Hyper**, el usuario puede obtener resultados de alta calidad sin necesidad de tener conocimientos técnicos avanzados.

Esta herramienta es ideal para exploraciones creativas y para generar contenido visual en diferentes ámbitos, facilitando la experimentación con diversos estilos y parámetros.
