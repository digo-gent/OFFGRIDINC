import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: 'static/js/main.js', // ✅ correct path from project root
    },
    outDir: 'static/dist',  // ✅ where built assets should go
    emptyOutDir: true,
  }
})
