document.addEventListener("DOMContentLoaded", () => {
    const year = document.getElementById("year");

    if (year) {
        year.textContent = new Date().getFullYear();
    }

    const starfield = document.getElementById("starfield");

    if (starfield) {
        const totalStars = 120;

        for (let index = 0; index < totalStars; index += 1) {
            const star = document.createElement("span");
            const size = 1 + Math.random() * 2.8;

            star.className = "star";
            star.style.width = `${size}px`;
            star.style.height = `${size}px`;
            star.style.left = `${Math.random() * 100}%`;
            star.style.top = `${Math.random() * 100}%`;
            star.style.opacity = `${0.3 + Math.random() * 0.7}`;
            star.style.animationDuration = `${5 + Math.random() * 10}s`;
            star.style.animationDelay = `${Math.random() * 8}s`;

            starfield.appendChild(star);
        }
    }

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
            }
        });
    }, {
        threshold: 0.16
    });

    document.querySelectorAll(".reveal").forEach((element) => {
        revealObserver.observe(element);
    });

    const counterEase = (value) => 1 - Math.pow(1 - value, 3);

    document.querySelectorAll("[data-count]").forEach((node) => {
        const targetValue = Number(node.getAttribute("data-count"));

        if (Number.isNaN(targetValue)) {
            return;
        }

        const duration = 1100;
        const startTime = performance.now();

        const animate = (now) => {
            const progress = Math.min((now - startTime) / duration, 1);
            const eased = counterEase(progress);
            const currentValue = Math.round(targetValue * eased);

            node.textContent = currentValue.toLocaleString();

            if (progress < 1) {
                requestAnimationFrame(animate);
            } else {
                node.textContent = targetValue.toLocaleString();
            }
        };

        requestAnimationFrame(animate);
    });

    const supportsHover = window.matchMedia("(hover: hover)").matches;

    if (supportsHover) {
        document.querySelectorAll(".tilt-card").forEach((card) => {
            card.addEventListener("mousemove", (event) => {
                const rect = card.getBoundingClientRect();
                const offsetX = (event.clientX - rect.left) / rect.width;
                const offsetY = (event.clientY - rect.top) / rect.height;
                const rotateY = (offsetX - 0.5) * 10;
                const rotateX = (0.5 - offsetY) * 10;

                card.style.transform = `perspective(1200px) translateY(-6px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
            });

            card.addEventListener("mouseleave", () => {
                card.style.transform = "";
            });
        });
    }
});