export function carousel(totalSlides) {
  return {
    current: 0,
    length: totalSlides,
    autoplay: null,

    get slidesPerView() {
      return window.innerWidth >= 768 ? 1 : 1;
    },

    init() {
      this.startAutoplay();
      window.addEventListener('resize', () => {
        this.current = Math.min(this.current, this.groupCount() - 1);
      });
    },

    next() {
      this.current = (this.current + 1) % this.groupCount();
    },

    prev() {
      this.current = (this.current - 1 + this.groupCount()) % this.groupCount();
    },

    groupCount() {
      return Math.ceil(this.length / this.slidesPerView);
    },

    startAutoplay() {
      this.autoplay = setInterval(() => this.next(), 6000);
    },

    stopAutoplay() {
      clearInterval(this.autoplay);
    }
  };
}
window.carousel = carousel;