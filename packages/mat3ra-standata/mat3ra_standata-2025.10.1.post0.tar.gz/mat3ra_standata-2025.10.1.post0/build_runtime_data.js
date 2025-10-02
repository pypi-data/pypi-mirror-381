/**
 * build_runtime_data uses node API to read all entity category files from the FS
 * at build time and writes them out to JSON files for
 * downstream consumption to avoid FS calls in the browser.
 */

/* eslint-disable @typescript-eslint/no-var-requires */
const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");
const BUILD_CONFIG = require("./build-config");

function buildAsset({
    assetPath,
    targetPath,
    contentGenerator = (content) => `${JSON.stringify(content)}\n`,
}) {
    const fileContent = fs.readFileSync(assetPath, { encoding: "utf-8" });
    const obj = {};
    obj.standataConfig = yaml.load(fileContent);

    obj.filesMapByName = {};

    // Check duplicate filenames for sanity
    const filenames = obj.standataConfig.entities.map((entity) => entity.filename);
    const duplicateFilenames = filenames.filter(
        (filename, index) => filenames.indexOf(filename) !== index,
    );
    if (duplicateFilenames.length > 0) {
        throw new Error(`Duplicate filenames found in ${assetPath}: ${duplicateFilenames}`);
    }
    // Create JSON
    obj.standataConfig.entities?.forEach((entity) => {
        const entityPath = path.join(path.dirname(assetPath), entity.filename);
        const content = fs.readFileSync(path.resolve(entityPath), { encoding: "utf-8" });
        console.log({ content, entityPath });
        obj.filesMapByName[entity.filename] = JSON.parse(content);
    });
    fs.writeFileSync(targetPath, contentGenerator(obj), "utf8");
    console.log(`Written entity category map to "${assetPath}" to "${targetPath}"`);
}

const { runtimeDataDir } = BUILD_CONFIG;

// JS Modules

buildAsset({
    assetPath: BUILD_CONFIG.categories.materials,
    targetPath: `${runtimeDataDir}/materials.json`,
});
buildAsset({
    assetPath: BUILD_CONFIG.categories.properties,
    targetPath: `${runtimeDataDir}/properties.json`,
});
buildAsset({
    assetPath: BUILD_CONFIG.categories.applications,
    targetPath: `${runtimeDataDir}/applications.json`,
});
buildAsset({
    assetPath: BUILD_CONFIG.categories.workflows,
    targetPath: `${runtimeDataDir}/workflows.json`,
});
buildAsset({
    assetPath: BUILD_CONFIG.categories.subworkflows,
    targetPath: `${runtimeDataDir}/subworkflows.json`,
});

function copyJsonAsset({ sourcePath, targetPath }) {
    if (fs.existsSync(sourcePath)) {
        const content = fs.readFileSync(sourcePath, "utf8");
        fs.writeFileSync(targetPath, content, "utf8");
        console.log(`Copied ${path.basename(sourcePath)} to "${targetPath}"`);
    } else {
        console.warn(`Warning: ${sourcePath} not found.`);
    }
}

// Copy JSON assets to runtime_data
copyJsonAsset({
    sourcePath: `./workflows/${BUILD_CONFIG.workflows.workflowSubforkflowMapByApplication}`,
    targetPath: `${runtimeDataDir}/${BUILD_CONFIG.workflows.workflowSubforkflowMapByApplication}`,
});

copyJsonAsset({
    sourcePath: `./applications/${BUILD_CONFIG.applications.modelMethodMapByApplication}`,
    targetPath: `${runtimeDataDir}/${BUILD_CONFIG.applications.modelMethodMapByApplication}`,
});

copyJsonAsset({
    sourcePath: `./applications/${BUILD_CONFIG.applications.templatesList}`,
    targetPath: `${runtimeDataDir}/${BUILD_CONFIG.applications.templatesList}`,
});

copyJsonAsset({
    sourcePath: `./applications/${BUILD_CONFIG.applications.executableFlavorMapByApplication}`,
    targetPath: `${runtimeDataDir}/${BUILD_CONFIG.applications.executableFlavorMapByApplication}`,
});

copyJsonAsset({
    sourcePath: `./applications/${BUILD_CONFIG.applications.applicationVersionsMapByApplication}`,
    targetPath: `${runtimeDataDir}/${BUILD_CONFIG.applications.applicationVersionsMapByApplication}`,
});

// Py Modules

buildAsset({
    assetPath: BUILD_CONFIG.categories.materials,
    targetPath: "./src/py/mat3ra/standata/data/materials.py",
    contentGenerator: (content) =>
        `import json\n\nmaterials_data = json.loads(r'''${JSON.stringify(content)}''')\n`,
});
buildAsset({
    assetPath: BUILD_CONFIG.categories.properties,
    targetPath: "./src/py/mat3ra/standata/data/properties.py",
    contentGenerator: (content) =>
        `import json\n\nproperties_data = json.loads(r'''${JSON.stringify(content)}''')\n`,
});
buildAsset({
    assetPath: BUILD_CONFIG.categories.applications,
    targetPath: "./src/py/mat3ra/standata/data/applications.py",
    contentGenerator: (content) =>
        `import json\n\napplications_data = json.loads(r'''${JSON.stringify(content)}''')\n`,
});
buildAsset({
    assetPath: BUILD_CONFIG.categories.workflows,
    targetPath: "./src/py/mat3ra/standata/data/workflows.py",
    contentGenerator: (content) =>
        `import json\n\nworkflows_data = json.loads(r'''${JSON.stringify(content)}''')\n`,
});
buildAsset({
    assetPath: BUILD_CONFIG.categories.subworkflows,
    targetPath: "./src/py/mat3ra/standata/data/subworkflows.py",
    contentGenerator: (content) =>
        `import json\n\nsubworkflows_data = json.loads(r'''${JSON.stringify(content)}''')\n`,
});
