# 🚀 GitHub Suite

A powerful Python-based GitHub analytics and monitoring toolkit that provides interactive visualizations and comprehensive repository insights.

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

## ✨ Features

- 📊 **Interactive Contribution Heatmap**: Visualize your GitHub activity patterns
- 🔍 **Dependency Security Scanner**: Check for vulnerabilities in your project dependencies
- 📈 **Activity Dashboard**: Track and analyze your GitHub events and interactions
- 📁 **Repository Management**: List and manage all your GitHub repositories
- 🔄 **Commit Tracker**: Monitor commits across all your repositories
- 📤 **Push Analytics**: Track push events and related statistics

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/TheRealSaiTama/Github-Suite.git
cd Github-Suite
```

2. Install required dependencies:
```bash
pip install requests json plotly numpy safety
```

## 🔑 Configuration

Before using the suite, you'll need to:

1. Generate a GitHub Personal Access Token:
   - Go to GitHub Settings → Developer Settings → Personal Access Tokens
   - Generate a new token with required permissions
   - Save the token securely

## 💻 Usage

Run the main script:
```bash
python suite.py
```

### Available Options:

1. **Generate GitHub Contributions Heatmap**
   - Visualizes your contribution patterns over time
   - Creates an interactive heatmap using Plotly

2. **Check Dependencies**
   - Scans project dependencies for known vulnerabilities
   - Provides detailed security advisories

3. **Generate GitHub Activity Dashboard**
   - Creates an interactive dashboard of your GitHub activity
   - Breaks down activities by type and frequency

4. **List User's Repositories**
   - Displays all repositories owned by the user
   - Includes repository names and basic information

5. **Show All Commits**
   - Lists commits across all repositories
   - Includes commit messages and authors

6. **Show All Pushes**
   - Tracks push events across repositories
   - Shows push authors and commit counts

## 📈 Features in Detail

### Contribution Heatmap
The heatmap provides a visual representation of your GitHub activity, similar to GitHub's contribution graph but with enhanced interactivity and customization options.

### Security Scanning
The dependency checker uses the `safety` package to scan your project's dependencies against known vulnerability databases, ensuring your project remains secure.

### Activity Dashboard
The dashboard offers insights into your GitHub activity patterns, helping you understand your workflow and identify areas for improvement.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the GitHub API for making this possible
- Plotly for the amazing visualization capabilities
- The Python community for the excellent packages

## 🔮 Future Enhancements

- [ ] Add support for organization analytics
- [ ] Implement more visualization types
- [ ] Add export functionality for reports
- [ ] Integrate with CI/CD pipelines
- [ ] Add custom alert systems

---

Created with ❤️ by [TheRealSaiTama](https://github.com/TheRealSaiTama)
