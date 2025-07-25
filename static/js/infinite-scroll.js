

document.addEventListener('alpine:init', () => {
  Alpine.directive('infinite-scroll', (el, { expression }, { evaluate }) => {
    // Add required classes
    el.classList.add('overflow-hidden', 'relative', 'whitespace-nowrap');

    const inner = el.querySelector('[data-scroll-content]');
    if (inner) {
      inner.classList.add('flex', 'animate-infinite-scroll');
    }

    // Set up hover pause
    el.addEventListener('mouseenter', () => {
      inner?.classList.add('paused');
    });

    el.addEventListener('mouseleave', () => {
      inner?.classList.remove('paused');
    });
  });
});
