// alpine-directives.js

import Alpine from 'alpinejs'
window.Alpine = Alpine
Alpine.start()

document.addEventListener('alpine:init', () => {
    Alpine.directive('fade-scroll', (el, { modifiers, expression }) => {
        let delay = modifiers.includes('delay') ? parseInt(expression) || 200 : 0;

        // Initial state
        el.classList.add(
            'transition',
            'duration-1000',
            'ease-in-out',
            'transform',
            'opacity-0',
            'translate-y-4'
        );

        const observer = new IntersectionObserver(([entry]) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    el.classList.remove('opacity-0', 'translate-y-4');
                    el.classList.add('opacity-100', 'translate-y-0');
                }, delay);
                observer.unobserve(el);
            }
        }, { threshold: 0.1 });

        observer.observe(el);
    });
});
