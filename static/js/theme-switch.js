// Toggle between dark and light themes. Saves preference to localStorage.
(function(){
    const root = document.documentElement;
    const toggleId = 'theme-toggle-btn';
    const storageKey = 'marketelite_theme';

    function applyTheme(theme){
        if(theme === 'light'){
            root.classList.add('light');
            root.setAttribute('data-theme','light');
        } else {
            root.classList.remove('light');
            root.setAttribute('data-theme','dark');
        }
    }

    // Initialize from localStorage or system preference
    const saved = localStorage.getItem(storageKey);
    if(saved){
        applyTheme(saved);
    } else {
        const prefersLight = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches;
        applyTheme(prefersLight ? 'light' : 'dark');
    }

    // Add click handler if button exists
    document.addEventListener('DOMContentLoaded', function(){
        const btn = document.getElementById(toggleId);
        if(!btn) return;
        // set initial icon
        function updateIcon(){
            const theme = root.classList.contains('light') ? 'light' : 'dark';
            btn.innerHTML = theme === 'light' ? '<i class="fas fa-moon"></i>' : '<i class="fas fa-sun"></i>';
        }
        updateIcon();

        btn.addEventListener('click', function(e){
            const isLight = root.classList.toggle('light');
            const newTheme = isLight ? 'light' : 'dark';
            localStorage.setItem(storageKey, newTheme);
            updateIcon();
        });
    });
})();
