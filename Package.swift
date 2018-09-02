// swift-tools-version:4.0
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "swift",
    dependencies: [
        .package(url: "https://github.com/Azoy/Sword", .branch("dev"))
    ],
    targets: [
        .target(
            name: "swift",
            dependencies: ["Sword"]),
    ]
)
