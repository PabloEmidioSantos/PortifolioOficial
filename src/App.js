import React from "react";

export default function App() {
    return (
        <>
            <header>Meu Portfólio</header>
            <nav>
                <a href="#home">Home</a>
                <a href="#about">Sobre Mim</a>
                <a href="#projects">Projetos</a>
                <a href="#contact">Contato</a>
            </nav>

            <section id="home">
                <h1>Olá, eu sou Pablo 👋</h1>
                <p>Desenvolvedor Full Stack e apaixonado por tecnologia!</p>
            </section>

            <section id="about">
                <h2>Sobre Mim</h2>
                <p>Tenho experiência com Node.js, React, e sempre buscando aprender mais.</p>
            </section>

            <section id="projects">
                <h2>Projetos</h2>
                <div className="project-card">Projeto 1</div>
                <div className="project-card">Projeto 2</div>
                <div className="project-card">Projeto 3</div>
            </section>

            <section id="contact">
                <h2>Contato</h2>
                <p>Email: pabloemidiosantos28@gmail.com</p>
            </section>
        </>
    );
}