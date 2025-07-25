// case_study.js

export function carousel(totalSlides) {
  return {
    current: 0,
    length: totalSlides,
    interval: null,

    init() {
      this.setSlidesPerView();
      this.clampCurrent();
      this.startAutoplay();
      window.addEventListener('resize', () => this.handleResize());
    },

    setSlidesPerView() {
      this.slidesPerView = window.innerWidth >= 768 ? 2 : 1;
    },

    clampCurrent() {
      const max = this.maxIndex();
      if (this.current > max) this.current = max;
    },

    handleResize() {
      this.setSlidesPerView();
      this.clampCurrent();
    },

    next() {
      const max = this.maxIndex();
      this.current = this.current >= max ? 0 : this.current + 1;
    },

    prev() {
      const max = this.maxIndex();
      this.current = this.current <= 0 ? max : this.current - 1;
    },

    startAutoplay() {
      this.stopAutoplay(); // prevent multiple intervals
      this.interval = setInterval(() => this.next(), 5000);
    },

    stopAutoplay() {
      if (this.interval) {
        clearInterval(this.interval);
        this.interval = null;
      }
    },

    goTo(index) {
      const max = this.maxIndex();
      this.current = Math.max(0, Math.min(index, max));
    },

    maxIndex() {
      return Math.ceil(this.length / this.slidesPerView) - 1;
    }
  };
}

// ✅ Make globally accessible for Alpine.js
window.carousel = carousel;
