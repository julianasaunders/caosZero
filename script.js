const body = document.body;
const toggleButton = document.getElementById('theme-toggle');
const toggleLabel = document.querySelector('.toggle-label');

const applyTheme = (theme) => {
  const resolvedTheme = theme === 'light' ? 'light' : 'dark';
  body.setAttribute('data-theme', resolvedTheme);
  toggleLabel.textContent = resolvedTheme === 'dark' ? 'Dark' : 'Light';
  localStorage.setItem('theme', resolvedTheme);
};

const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
  applyTheme(savedTheme);
} else {
  applyTheme('dark');
}

toggleButton.addEventListener('click', () => {
  const currentTheme = body.getAttribute('data-theme');
  const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
  applyTheme(nextTheme);
});
