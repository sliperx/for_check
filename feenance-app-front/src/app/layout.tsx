import "./reset.css";
import "./globals.css";

import ProviderList from "../services/redux/provider";

import type { Metadata } from "next";

export const metadata: Metadata = {
	title: "freenance",
	description: "Generated by create next app",
};

export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return (
		<html lang="en">
			<body>
				<ProviderList>{children}</ProviderList>
			</body>
		</html>
	);
}