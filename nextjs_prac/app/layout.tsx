import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
    title: "My Website",
    description: "A description of my website",
};

export default function RootLayout({
    children,
    }: Readonly<{
        children: React.ReactNode;
    }>) {
        return (
            <html lang="en">
                <body>  
                    <header>
                        <nav>
                            <a href="/">Home</a>
                            <a href="/about">About</a>
                        </nav>
                    </header>

                    <main>{children}</main>

                    <footer>
                        <p>@ 2026 My website</p>
                    </footer>
                </body>
            </html>
        );
    }
