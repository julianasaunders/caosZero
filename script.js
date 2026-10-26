const body = document.body;
const toggleButton = document.getElementById('theme-toggle');
const toggleLabel = document.querySelector('.toggle-label');
const statFiles = document.getElementById('stat-files');
const statTime = document.getElementById('stat-time');
const statCategories = document.getElementById('stat-categories');
const folderList = document.querySelector('.folder-list');
const addFolderButton = document.getElementById('add-folder-button');
const folderInput = document.getElementById('folder-input');

const projectCategories = {
  Documentos: ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
  Imagens: ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
  Videos: ['.mp4', '.mkv', '.avi', '.mov'],
  Compactados: ['.zip', '.tar.gz', '.rar', '.7z'],
  Executaveis_Scripts: ['.sh', '.py', '.bin', '.deb'],
};

const formatSeconds = (value) => {
  const safeValue = Math.max(1, Math.round(value));
  return `${String(safeValue).padStart(2, '0')}s`;
};

const getFileCategory = (fileName) => {
  const lowerName = fileName.toLowerCase();

  for (const [category, extensions] of Object.entries(projectCategories)) {
    const matched = extensions.some((extension) => lowerName.endsWith(extension.toLowerCase()));
    if (matched) {
      return category;
    }
  }

  return 'Outros';
};

const renderFolderList = (items) => {
  folderList.innerHTML = '';

  items.forEach((item) => {
    const folderItem = document.createElement('div');
    folderItem.className = 'folder-item';

    const folderName = document.createElement('span');
    folderName.className = 'folder-name';
    folderName.textContent = item.name;

    const folderCount = document.createElement('span');
    folderCount.className = 'folder-count';
    folderCount.textContent = item.count.toLocaleString('pt-BR');

    folderItem.append(folderName, folderCount);
    folderList.appendChild(folderItem);
  });
};

const updateStats = (stats) => {
  const totalFiles = stats.reduce((sum, item) => sum + item.count, 0);
  const totalCategories = stats.filter((item) => item.count > 0).length;
  const averageSeconds = totalFiles > 0 ? Math.max(1, Math.round(totalFiles / 28)) : 1;

  statFiles.textContent = totalFiles.toLocaleString('pt-BR');
  statTime.textContent = formatSeconds(averageSeconds);
  statCategories.textContent = String(totalCategories || 1);

  const orderedStats = Object.entries(projectCategories).map(([name]) => ({
    name,
    count: stats.find((item) => item.name === name)?.count ?? 0,
  }));

  renderFolderList(orderedStats.filter((item) => item.count > 0));
};

const readFolderFiles = (files) => {
  const categoryCounts = Object.keys(projectCategories).map((name) => ({ name, count: 0 }));

  files.forEach((file) => {
    if (!file || typeof file.name !== 'string') {
      return;
    }

    const categoryName = getFileCategory(file.name);
    const categoryFound = categoryCounts.find((item) => item.name === categoryName);

    if (categoryFound) {
      categoryFound.count += 1;
    }
  });

  updateStats(categoryCounts);
};

const handleFolderSelection = (event) => {
  const files = Array.from(event.target.files || []);

  if (!files.length) {
    return;
  }

  readFolderFiles(files);
};

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

addFolderButton.addEventListener('click', () => {
  folderInput.click();
});

folderInput.addEventListener('change', handleFolderSelection);

const defaultStats = Object.entries(projectCategories).map(([name]) => ({ name, count: 0 }));
updateStats(defaultStats);
