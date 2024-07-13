\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{bpraxis}[BPraxis]
\LoadClass[12pt]{article}

\RequirePackage[
a4paper,
top=3.5cm,
bottom=2.5cm,
left=2.5cm,
right=2.5cm,
marginparwidth=1.75cm,
headsep=1cm,
% showframe=true,
]{geometry}
\RequirePackage{xparse}
\RequirePackage[german]{babel}
\RequirePackage[utf8]{inputenc}
\RequirePackage{fontspec}
\RequirePackage{xcolor}
\RequirePackage{colortbl}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{titlesec}
\RequirePackage{enumitem}
\RequirePackage[hidelinks]{hyperref}
\RequirePackage{tabularx}
\RequirePackage{caption}
\RequirePackage{subcaption}
\RequirePackage{multicol}
\RequirePackage{float}
\RequirePackage{listings}
\RequirePackage{soul}

\setmainfont{Georgia}

\definecolor{lighblue}{RGB}{0, 147, 210}
\definecolor{lightgray}{gray}{0.85}
\definecolor{lightergray}{gray}{0.96}
\definecolor{dkgreen}{rgb}{0,0.6,0}
\definecolor{gray}{rgb}{0.5,0.5,0.5}
\definecolor{mauve}{rgb}{0.58,0,0.82}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{Bericht Praxistätigkeit FS24}
\fancyfoot[L]{\hypersetup{linkcolor=black}Seite \thepage{} von \pageref{LastPage}}
\fancyfoot[R]{13.07.2024}

\titlespacing*{\section}{0pt}{0pt}{0pt}
\titlespacing*{\subsection}{0pt}{0pt}{-4pt}
\titlespacing*{\subsubsection}{0pt}{0pt}{-4pt}

\setlength{\parindent}{0pt}
\setlength{\parskip}{10pt}

\setlist{nosep}
\hypersetup{%
  colorlinks=true,%
  linkcolor=lighblue,%
  linkbordercolor=lighblue,%
  urlcolor=lighblue,%
  urlbordercolor=lighblue,%
  pdfborderstyle={/S/U/W 1.5}%
}

\newcolumntype{L}[0]{@{}>{\raggedright\arraybackslash}X@{}}
\newcolumntype{C}[0]{@{}>{\centering\arraybackslash}X@{}}
\newcolumntype{R}[0]{@{}>{\raggedleft\arraybackslash}X@{}}
\newcolumntype{P}[1]{@{}>{\raggedright\arraybackslash}p{#1}@{}}
\newcolumntype{Q}[1]{@{}>{\raggedleft\arraybackslash}p{#1}@{}}

\setlength{\arrayrulewidth}{0.5pt}

\lstset{
  language=Python,
  aboveskip=3mm,
  belowskip=3mm,
  showstringspaces=false,
  columns=flexible,
  basicstyle={\small\ttfamily},
  numbers=none,
  numberstyle=\tiny\color{gray},
  keywordstyle=\color{blue},
  commentstyle=\color{dkgreen},
  stringstyle=\color{mauve},
  backgroundcolor=\color{lightergray},
  frame=tlbr,
  framesep=5pt,
  framerule=0pt,
  breaklines=true,
  breakatwhitespace=true,
  tabsize=2,
}

% custom commands
\makeatletter
\def\MaxGraphicsWidth#1{%
  \ifdim\Gin@nat@width>#1 #1\else\Gin@nat@width\fi%
}
\def\MaxGraphicsHeight#1{%
  \ifdim\Gin@nat@height>#1 #1\else\Gin@nat@height\fi%
}
\makeatother

\newcommand{\RemainingTextWidth}[1]{%
  \dimexpr\textwidth-#1\relax%
}

\newcommand{\SizedText}[2]{{%
  \fontsize{#1}{1.2\baselineskip}\selectfont#2%
}}

\newcommand{\ColoredText}[3]{{%
  \fontsize{#2}{1.2\baselineskip}\selectfont%
  \textcolor{#1}{#3}%
}}

\newcommand{\FigureSingle}[3][\linewidth]{
  \begin{figure}[H]
    \includegraphics[width=#1]{#2}
    \captionsetup{singlelinecheck=false, justification=raggedright}
    \caption{#3}
    \label{fig:#2}
  \end{figure}
}

\newcommand{\FigureDouble}[5][0.45\linewidth]{
  \begin{figure}[H]
    \begin{minipage}{#1}
      \centering
      \includegraphics[width=\linewidth]{#2}
      \caption{#3}
      \label{fig:#2}
    \end{minipage}%
    \hfill
    \begin{minipage}{#1}
      \centering
      \includegraphics[width=\linewidth]{#4}
      \caption{#5}
      \label{fig:#4}
    \end{minipage}
  \end{figure}
}

\newcommand{\FigureTriple}[7][0.3\linewidth]{
  \begin{figure}[H]
    \begin{minipage}{#1}
      \centering
      \includegraphics[width=\linewidth]{#2}
      \caption{#3}
      \label{fig:#2}
    \end{minipage}%
    \hfill
    \begin{minipage}{#1}
      \centering
      \includegraphics[width=\linewidth]{#4}
      \caption{#5}
      \label{fig:#4}
    \end{minipage}
    \hfill
    \begin{minipage}{#1}
      \centering
      \includegraphics[width=\linewidth]{#6}
      \caption{#7}
      \label{fig:#6}
    \end{minipage}
  \end{figure}
}

\newcommand{\Code}[1]{\sethlcolor{lightergray}\hl{\texttt{#1}}}

\newcommand{\ImportCode}[3][Python]{
  \lstinputlisting[language=#1,caption={#2},label={lst:#3}]{code/#3}
}
