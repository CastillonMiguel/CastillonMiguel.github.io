.. :html_theme.sidebar_secondary.remove:

.. raw:: html

    <style type="text/css">
        .hero-section {
            background: linear-gradient(135deg, #2c5f75 0%, #1e3a5f 100%);
            color: white;
            padding: 3rem 2rem;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        .hero-title {
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            color: white;
        }
        .hero-subtitle {
            font-size: 1.5rem;
            opacity: 0.9;
            margin-bottom: 1rem;
        }
        .hero-description {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto 1.5rem;
            opacity: 0.95;
        }
        .hero-button {
            display: inline-block;
            background: #00c6cf;
            color: white !important;
            padding: 0.8rem 1.5rem;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 198, 207, 0.3);
        }
        .hero-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 198, 207, 0.5);
        }
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }
        .skill-card {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            border-left: 5px solid #2c5f75;
        }
        .skill-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        .skill-card a {
            text-decoration: none;
            color: inherit;
        }
        .skill-icon {
            font-size: 2rem;
            margin-bottom: 1rem;
        }
        .skill-title {
            font-size: 1.3rem;
            font-weight: bold;
            color: #333;
            margin-bottom: 0.5rem;
        }
        .skill-description {
            color: #666;
            line-height: 1.6;
        }
        .interests-section {
            background: #f8f9fa;
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
        }
        .interests-title {
            text-align: center;
            font-size: 2rem;
            font-weight: bold;
            color: #333;
            margin-bottom: 1.5rem;
        }
        .interests-list {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 1rem;
        }
        .interest-item {
            background: white;
            padding: 0.8rem 1.5rem;
            border-radius: 25px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            font-size: 1.1rem;
            transition: all 0.3s ease;
        }
        .interest-item:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        [data-theme="dark"] .interest-item {
            color: black;
        }
    </style>

    <div class="hero-section">
        <h1 class="hero-title">Miguel Castillón</h1>
        <p class="hero-subtitle">Research Scientist</p>
        <p class="hero-description">
            I am driving innovation in computational mechanics, with a focus on phase-field models, the finite element method, and advanced numerical methods.
        </p>
        <a href="Publications/index.html" class="hero-button">View My Publications 📄</a>
    </div>

    <div class="skills-grid">
        <div class="skill-card">
            <a href="https://github.com/CastillonMiguel" target="_blank">
                <img src="_static/github-mark.png" alt="GitHub Profile" class="skill-icon" style="width: 40px; height: 40px; border-radius: 50%;">
                <div class="skill-title">GitHub Profile</div>
                <div class="skill-description">
                    Explore my open-source projects, including the implementation of phase-field models and other computational tools.
                </div>
            </a>
        </div>
        
        <div class="skill-card">
            <a href="https://phasefieldx.readthedocs.io" target="_blank">
                <img src="_static/logo_social.png" alt="phasefieldx logo" class="skill-icon" style="width: 100px; border-radius: 50%;">
                <div class="skill-title">PhaseFieldX Documentation</div>
                <div class="skill-description">
                    Access the comprehensive documentation for the PhaseFieldX Python library, including tutorials and API references.
                </div>
            </a>
        </div>

        <div class="skill-card">
            <a href="https://doi.org/10.1016/j.ijfatigue.2025.109397" target="_blank">
                <div class="skill-icon">📄</div>
                <div class="skill-title">Fatigue Analysis Journal Paper</div>
                <div class="skill-description">
                    Check out the novel phase-field approach to fatigue analysis, published in the International Journal of Fatigue.
                </div>
            </a>
        </div>

        <div class="skill-card">
            <a href="Utils/index.html" target="_blank">
                <div class="skill-icon">🛠️</div>
                <div class="skill-title">Research Utilities</div>
                <div class="skill-description">
                    Discover a collection of tools and guides for researchers, including tips on LaTeX, repository structure, and more.
                </div>
            </a>
        </div>
    </div>

    <div class="interests-section">
        <h2 class="interests-title">Interests</h2>
        <div class="interests-list">
            <div class="interest-item">📚 Research</div>
            <div class="interest-item">💡 Innovation</div>
            <div class="interest-item">🔧 Topology Optimization</div>
            <div class="interest-item">🖨️ 3D Printing</div>
            <div class="interest-item">⚙️ Multibody Systems</div>
            <div class="interest-item">🏎️ Vehicle Dynamics</div>
            <div class="interest-item">💻 Programming</div>
            <div class="interest-item">🛠️ Development Tools</div>
            <div class="interest-item">⚡ Code Optimization</div>
            <div class="interest-item">🖥️ Supercomputing</div>
            <div class="interest-item">⚖️ Parallel Computing</div>
            <div class="interest-item">🔬 Computational Mechanics</div>
        </div>
    </div>

.. include:: Contact/index.rst

Content 📚
**********
.. toctree::
   :maxdepth: 1
   
   AboutMe/index
   Projects/index
   Publications/index
   Utils/index
   Contact/index
