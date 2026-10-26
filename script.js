const body = document.body;
const toggleButton = document.getElementById('theme-toggle');
const statFiles = document.getElementById('stat-files');
const statTime = document.getElementById('stat-time');
const statCategories = document.getElementById('stat-categories');
const folderList = document.querySelector('.folder-list');
const addFolderButton = document.getElementById('add-folder-button');

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

  if (!items.length) {
    const emptyItem = document.createElement('div');
    emptyItem.className = 'folder-item';
    emptyItem.innerHTML = '<span class="folder-name">Nenhuma pasta</span><span class="folder-count">0</span>';
    folderList.appendChild(emptyItem);
    return;
  }

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

  if (totalFiles === 0) {
    statFiles.textContent = '0';
    statTime.textContent = '00s';
    statCategories.textContent = '0';
    renderFolderList([]);
    return;
  }

  const averageSeconds = Math.max(1, Math.round(totalFiles / 28));

  statFiles.textContent = totalFiles.toLocaleString('pt-BR');
  statTime.textContent = formatSeconds(averageSeconds);
  statCategories.textContent = String(totalCategories);

  const orderedStats = Object.entries(projectCategories).map(([name]) => ({
    name,
    count: stats.find((item) => item.name === name)?.count ?? 0,
  }));

  renderFolderList(orderedStats.filter((item) => item.count > 0));
};

const analyzeFolderEntries = (files) => {
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

const organizeDirectoryHandle = async (directoryHandle) => {
  const fileEntries = [];

  for await (const [name, handle] of directoryHandle.entries()) {
    if (handle.kind === 'file') {
      fileEntries.push({ name, handle });
    }
  }

  const categoryCounts = Object.keys(projectCategories).map((name) => ({ name, count: 0 }));

  for (const entry of fileEntries) {
    const categoryName = getFileCategory(entry.name);
    const categoryFound = categoryCounts.find((item) => item.name === categoryName);

    if (!categoryFound) {
      continue;
    }

    const categoryFolder = await directoryHandle.getDirectoryHandle(categoryName, { create: true });
    const destinationFile = await categoryFolder.getFileHandle(entry.name, { create: true });
    const fileData = await entry.handle.getFile();
    const writable = await destinationFile.createWritable();
    await writable.write(await fileData.arrayBuffer());
    await writable.close();
    await directoryHandle.removeEntry(entry.name);
    categoryFound.count += 1;
  }

  updateStats(categoryCounts);
};

const handleDirectorySelection = async () => {
  if (!('showDirectoryPicker' in window)) {
    alert('Seu navegador não suporta a seleção direta de pastas. Use o Chrome/Edge mais recente.');
    return;
  }

  try {
    const directoryHandle = await window.showDirectoryPicker({ mode: 'readwrite' });
    await organizeDirectoryHandle(directoryHandle);
  } catch (error) {
    console.error('Erro ao acessar a pasta:', error);
  }
};

const applyTheme = (theme) => {
  const resolvedTheme = theme === 'light' ? 'light' : 'dark';
  body.setAttribute('data-theme', resolvedTheme);
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

addFolderButton.addEventListener('click', handleDirectorySelection);

const defaultStats = Object.entries(projectCategories).map(([name]) => ({ name, count: 0 }));
updateStats(defaultStats);
