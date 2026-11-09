<style>
  img[src*="shields.io"] {
    border: none !important;
    box-shadow: none !important;
    margin: 2px !important;
    padding: 0 !important;
  }
  .hero-gif {
    border-radius: 6px;
    border: 1px solid #30363d !important;
    max-width: 100%;
    height: auto;
  }
  .nav-bar {
    background: #161b22;
    border: 1px solid #30363d;
    padding: 12px;
    border-radius: 6px;
    text-align: center;
    margin-bottom: 25px;
  }
  .nav-bar a {
    color: #58a6ff;
    margin: 0 14px;
    font-weight: 600;
    text-decoration: none;
  }
  .nav-bar a:hover {
    text-decoration: underline;
  }
  .project-card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 18px;
    margin-bottom: 16px;
    color: #c9d1d9;
  }
  .project-card h4 {
    margin-top: 0;
    margin-bottom: 8px;
    color: #58a6ff;
  }
  .pub-category {
    color: #58a6ff;
    margin-top: 20px;
    margin-bottom: 10px;
    border-bottom: 1px solid #30363d;
    padding-bottom: 4px;
  }
</style>

<div class="nav-bar">
  <a href="#perfil">Perfil</a> |
  <a href="#projetos">Projetos e Sistemas</a> |
  <a href="#pesquisa">Produção Científica</a> |
  <a href="#competencias">Stack Tecnológica</a> |
  <a href="#contato">Contato</a>
</div>

<div align="center">
  <a href="https://www.linkedin.com/in/lucenildo-cerqueira-2534b228/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://scholar.google.com/citations?user=sbiFXRIAAAAJ&hl=pt-BR"><img src="https://img.shields.io/badge/Google_Scholar-4285F4?style=for-the-badge&logo=google-scholar&logoColor=white" alt="Google Scholar"></a>
  <a href="https://publons.com/wos-op/researcher/2495914/lucenildo-s-cerqueira/"><img src="https://img.shields.io/badge/Web_of_Science-5E33BF?style=for-the-badge&logo=clarivate&logoColor=white" alt="Web of Science"></a>
  <a href="https://www.kaggle.com/lucenildocerqueira"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" alt="Kaggle"></a>
  <a href="https://github.com/lucecerqueira"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="mailto:lucecerqueira@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"></a>
</div>

<br>

<p align="center">
  <img class="hero-gif" src="./vcg_mit.gif" alt="Processamento de Sinais Biomédicos - Vetorcardiograma 3D" width="500" />
  <br>
  <em>Reconstrução espacial e análise dinâmica de sinais cardíacos (Vetorcardiograma 3D).</em>
</p>

---

## <a id="perfil"></a>Perfil Profissional

Sou **Cientista de Dados** e **Doutor (DSc.) em Ciências / Engenharia Biomédica** (PEB/COPPE/UFRJ), com atuação na interseção entre modelagem matemática, aprendizado de máquina (Machine e Deep Learning), engenharia de dados em saúde pública e desenvolvimento de sistemas analíticos.

* **Ciência de Dados e IA em Saúde:** Desenvolvimento de modelos preditivos, classificação diagnóstica de sinais eletrofisiológicos (ECG, VCG e EMG), regulação autonômica, vigilância epidemiológica e análise espacial em oncologia.
* **Engenharia de Software e Dados:** Arquitetura de pipelines ETL de alto desempenho para grandes bases governamentais (DATASUS/SIM) e desenvolvimento de aplicações web e painéis interativos (Python, Django, R/Shiny, PostgreSQL).
* **Fisiologia e Biomecânica Computacional:** Modelagem não-linear de cinética cardiorrespiratória ($\dot{V}O_2$), cinemática da locomoção, ajuste de curvas multiparamétricas e análise de tempo de reação cognitiva.

---

## <a id="projetos"></a>Projetos e Sistemas em Destaque

<div class="project-card">
  <h4>Classificação Diagnóstica de ECG e Vetorcardiograma 3D com Machine Learning</h4>
  <p>Pipeline de processamento de sinais biomédicos e inteligência artificial para detecção de Infarto do Miocárdio, eventos isquêmicos e alterações de ST-T utilizando reconstrução espacial tridimensional do vetorcardiograma (VCG) e Redes Neurais.</p>
  <p><strong>Tecnologias:</strong> Python, Scikit-Learn, Keras, Processamento Digital de Sinais (DSP).</p>
</div>

<div class="project-card">
  <h4>Plataforma de Vigilância Oncológica e Pipeline ETL (SIM/DATASUS)</h4>
  <p>Ecossistema para extração, descompactação nativa, transformação e carga (ETL) de microdados do Sistema de Informações sobre Mortalidade (SIM/DATASUS) integrado a painel geoespacial interativo para análise epidemiológica.</p>
  <p><strong>Tecnologias:</strong> R, Shiny (bs4Dash, Leaflet, Plotly), Python, Django, PostgreSQL, C.</p>
</div>

<div class="project-card">
  <h4>Sistema de Apoio à Decisão Clínica (Predição de Lesão Renal Aguda)</h4>
  <p>Aplicação web voltada à estratificação de risco clínico para rabdomiólise e lesão renal aguda, equipada com sincronização offline e geração automatizada de relatórios técnicos em PDF.</p>
  <p><strong>Tecnologias:</strong> Python, Django, PostgreSQL, Modelagem Estatística.</p>
</div>

<div class="project-card">
  <h4>Plataforma Analítica para Eco-hidrologia e Qualidade da Água</h4>
  <p>Sistema web estruturado para gerenciamento de dados ambientais, análises estatísticas e monitoramento de parâmetros de potabilidade e eco-hidrologia.</p>
  <p><strong>Tecnologias:</strong> Python, Django, PostgreSQL, Pandas, Plotly.</p>
</div>

<div class="project-card">
  <h4>NeuroPulse — Análise de Tempo de Reação Cognitiva</h4>
  <p>Aplicação de alta precisão temporal para avaliação neurocognitiva e biomecânica executada diretamente no navegador com latência mínima.</p>
  <p><strong>Tecnologias:</strong> Rust, WebAssembly (WASM), Leptos.</p>
</div>

---

## <a id="pesquisa"></a>Produção Científica e Publicações Selecionadas

Lista completa de artigos, citações e métricas acadêmicas disponível no [Google Scholar](https://scholar.google.com/citations?user=sbiFXRIAAAAJ&hl=pt-BR) e na [Web of Science (ResearcherID)](https://publons.com/wos-op/researcher/2495914/lucenildo-s-cerqueira/).

<h4 class="pub-category">Inteligência Artificial, Eletrocardiografia (ECG/VCG) e Engenharia Biomédica</h4>

* **Diagnostic ECG Classification of Myocardial Infarction and ST-T Changes Using Machine Learning via 3D Vectorcardiogram.** *Computing in Cardiology (CinC)*, 2025.
* **Detecção de Eventos Isquêmicos e Diagnóstico de Infarto via Vetorcardiograma e Redes Neurais Convolucionais / Análise Bibliométrica Computacional.** *Congresso Brasileiro de Engenharia Biomédica (CBEB)*, 2024.

<h4 class="pub-category">Biomecânica Computacional, Cinemática e Processamento de Sinais</h4>

* **Biomechanical alterations of gait on overweight subjects.** *Research on Biomedical Engineering*, 2018.
* **Comparison of five kinematic-based identification methods of foot contact events during treadmill walking and running at different speeds.** *Journal of Applied Biomechanics*, 2015.

<h4 class="pub-category">Fisiologia do Exercício, Cinética de VO2, Eletromiografia e Saúde</h4>

* **Estudos sobre cinética cardiorrespiratória ($\dot{V}O_2$), relações metabólicas e análise eletromiográfica (EMG).** Publicações em periódicos revisados por pares incluindo *European Journal of Applied Physiology*, *Revista Brasileira de Medicina do Esporte* e *Revista de Nutrição*.
* **Relação entre esporte, resiliência, qualidade de vida e ansiedade.** *Archives of Clinical Psychiatry (São Paulo)*, 2012.

---

## <a id="competencias"></a>Stack Tecnológica

### Linguagens, Bancos de Dados e Ambiente
![Python](https://img.shields.io/badge/Python-14354C?style=flat-square&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)
![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=flat-square&logo=mongodb&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

### Ciência de Dados, Machine Learning e Visualização
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=Keras&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white)

### Desenvolvimento Web, Engenharia de Dados e Infraestrutura
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![Shiny](https://img.shields.io/badge/R_Shiny-276DC3?style=flat-square&logo=r&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat-square&logo=apachespark&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=Apache%20Airflow&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=flat-square&logo=elasticsearch&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)

---

## <a id="contato"></a>Contato

* **E-mail:** [lucecerqueira@gmail.com](mailto:lucecerqueira@gmail.com)
* **LinkedIn:** [linkedin.com/in/lucenildo-cerqueira-2534b228](https://www.linkedin.com/in/lucenildo-cerqueira-2534b228/)
* **Google Scholar:** [scholar.google.com/citations?user=sbiFXRIAAAAJ](https://scholar.google.com/citations?user=sbiFXRIAAAAJ&hl=pt-BR)
* **Web of Science:** [ResearcherID: 2495914](https://publons.com/wos-op/researcher/2495914/lucenildo-s-cerqueira/)
* **GitHub:** [github.com/lucecerqueira](https://github.com/lucecerqueira)

---
<p align="center">
  <small>Lucenildo Silva Cerqueira, DSc. — Licenciado sob <a href="./LICENSE">MIT License</a>.</small>
</p>
